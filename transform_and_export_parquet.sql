-- Crear la tabla nasdaq_data especificando tipos de datos
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

-- Insertar datos desde el CSV, manejando valores NA
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
FROM read_csv_auto('NASDAQ 1962-2024.csv', HEADER=TRUE, types={'Open': 'VARCHAR', 'High': 'VARCHAR', 'Low': 'VARCHAR', 'Close': 'VARCHAR', 'Adj Close': 'VARCHAR', 'Volume': 'VARCHAR'});

-- Exportar la tabla a formato Parquet
COPY nasdaq_data TO 'nasdaq_data_export.parquet' (FORMAT PARQUET);
