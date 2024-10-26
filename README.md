#  Process Automation for Data Analytics with DuckDB, using Docker container.
This project demonstrates the automation of data analytics processes using DuckDB within a Docker container environment.

## Summary of Key Components:

    Docker Container Configuration: A Docker container was configured with Ubuntu and the necessary dependencies to support DuckDB installation from the GitHub repository.

    DuckDB as an In-Memory Database: DuckDB serves as an efficient in-memory database, enabling real-time data processing and complex computations.

    Table Creation: A table structure was created to store NASDAQ stock data, with explicit handling for NAN values to maintain data integrity.
    
    Data Persistence: Persist data in Parquet format, ensuring efficient storage and accessibility for future analysis.

    SQL Query Implementation: Various SQL queries were executed to derive meaningful insights, such as total trade volume per year and stock performance metrics.

    Automation with Python: Python scripts were utilized to automate data processes, further enhancing the analytical capabilities of the system.

## Report of results:

### Configuration of a docker container:
Installed an Ubuntu machine with the necessary dependencies


### Install DuckDB from Github repository:


### Run DuckDB as in-memory database.
Set up DuckDB to function as an in-memory database for rapid data analysis.


### Creation of tables in DuckDB:
Created necessary tables to structure and manage stock data effectively.


### NAN values transformations:
Implemented transformations to handle NAN values during data ingestion to ensure data quality.


## Example of "Total Trade Volume per Year" query:
Showcased an example query that aggregates total trading volume by year for analysis.


## Execution of commands directly from the shell:
Executed a .sql file that automates table generation and data processing.


## Example of how to persist data with DuckDB BBDD format:
Illustrated methods for persisting data in DuckDB database format.


## Example of automatitation of data process using python scripts:
Demonstrated automation techniques utilizing Python scripts for data processing tasks.