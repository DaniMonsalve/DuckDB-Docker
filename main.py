import duckdb

# Connect to DuckDB (you can specify a file if you want)
con = duckdb.connect()  # In-memory connection

# Create the nasdaq_data table specifying data types
con.execute("""
CREATE TABLE nasdaq_data (
    "Date" DATE,
    "Ticker" VARCHAR,
    "Exchange" VARCHAR,
    "Open" DOUBLE,
    "High" DOUBLE,
    "Low" DOUBLE,
    "Close" DOUBLE,
    "Adj Close" DOUBLE,
    "Volume" DOUBLE
);
""")

# Insert data from the CSV, handling NA values
con.execute("""
INSERT INTO nasdaq_data
SELECT 
    "Date",
    "Ticker",
    "Exchange",
    NULLIF("Open", 'NA')::DOUBLE AS "Open",
    NULLIF("High", 'NA')::DOUBLE AS "High",
    NULLIF("Low", 'NA')::DOUBLE AS "Low",
    NULLIF("Close", 'NA')::DOUBLE AS "Close",
    NULLIF("Adj Close", 'NA')::DOUBLE AS "Adj Close",
    NULLIF("Volume", 'NA')::DOUBLE AS "Volume"
FROM read_csv_auto('/poc/NASDAQ 1962-2024.csv', HEADER=TRUE, types={
    'Open': 'VARCHAR', 
    'High': 'VARCHAR', 
    'Low': 'VARCHAR', 
    'Close': 'VARCHAR', 
    'Adj Close': 'VARCHAR', 
    'Volume': 'VARCHAR'
});
""")

# Business logic queries

# 1. Get the highest and lowest closing prices in history
highest_close = con.execute("SELECT MAX(Close) AS Max_Close, MIN(Close) AS Min_Close FROM nasdaq_data;").fetchall()
print("Highest and Lowest Closing Prices:", highest_close)

# 2. Calculate the average trading volume per stock
average_volume = con.execute("SELECT Ticker, AVG(Volume) AS Average_Volume FROM nasdaq_data GROUP BY Ticker;").fetchall()
print("Average Trading Volume per Stock:", average_volume)

# 3. Find the day with the largest increase in closing price
largest_increase = con.execute("""
SELECT "Date", Ticker, (Close - LAG(Close) OVER (PARTITION BY Ticker ORDER BY "Date")) AS Price_Increase
FROM nasdaq_data
WHERE Price_Increase IS NOT NULL
ORDER BY Price_Increase DESC
LIMIT 1;
""").fetchall()
print("Day with the Largest Increase in Closing Price:", largest_increase)

# 4. Get the stock with the highest average opening price
highest_average_open = con.execute("""
SELECT Ticker, AVG(Open) AS Avg_Open
FROM nasdaq_data
GROUP BY Ticker
ORDER BY Avg_Open DESC
LIMIT 1;
""").fetchall()
print("Stock with the Highest Average Opening Price:", highest_average_open)

# 5. Calculate the percentage return of closing prices in the last year
last_year_return = con.execute("""
SELECT Ticker, 
       ((MAX(Close) - MIN(Close)) / MIN(Close)) * 100 AS Percent_Return
FROM nasdaq_data
WHERE "Date" >= DATEADD('year', -1, CURRENT_DATE)
GROUP BY Ticker;
""").fetchall()
print("Percentage Return of Closing Prices in the Last Year:", last_year_return)

# If you need to verify the table
result = con.execute("SELECT * FROM nasdaq_data LIMIT 10;").fetchall()
print("First 10 Rows of the nasdaq_data Table:", result)

# Close the connection
con.close()

