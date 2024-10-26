#  Process Automation for Data Analytics with DuckDB, using Docker container.
This project demonstrates the automation of data analytics processes using DuckDB within a Docker container environment.

## Summary of Key Components:

- **Docker Container Configuration**: A Docker container was configured with Ubuntu and the necessary dependencies to support DuckDB installation from the GitHub repository.

- **DuckDB as an In-Memory Database**: DuckDB serves as an efficient in-memory database, enabling real-time data processing and complex computations.

- **Table Creation**: A table structure was created to store NASDAQ stock data, with explicit handling for NAN values to maintain data integrity.
    
- **Data Persistence**: Persist data in Parquet format, ensuring efficient storage and accessibility for future analysis.

- **SQL Query Implementation**: Various SQL queries were executed to derive meaningful insights, such as total trade volume per year and stock performance metrics.

- **Automation with Python**: Python scripts were utilized to automate data processes, further enhancing the analytical capabilities of the system.

## Report of results:

### Configuration of a docker container:
Installed an Ubuntu machine with the necessary dependencies
<img width="953" alt="Arrancamos un contenedor con Ubuntu" src="https://github.com/user-attachments/assets/1a0c5ffc-1b57-4bd8-9526-5e570e7c86f4">
<img width="954" alt="Containers - Docker Desktop" src="https://github.com/user-attachments/assets/f27445eb-6025-4e94-bfb4-242106bbaf0c">


### Install DuckDB from Github repository:
<img width="949" alt="Install DuckDB from Github" src="https://github.com/user-attachments/assets/a75a1359-6605-4e6d-a676-7c32dc5ff47a">


### Run DuckDB as in-memory database.
Set up DuckDB to function as an in-memory database for rapid data analysis.
<img width="846" alt="Run DuckDB" src="https://github.com/user-attachments/assets/c27b72de-d05d-49bc-ac8f-42364d47002a">


### Creation of tables in DuckDB:
Created necessary tables to structure and manage stock data effectively.
<img width="956" alt="Create tables in DuckDB" src="https://github.com/user-attachments/assets/607ca447-28e1-478f-b113-ffa025f0bbdf">


### NAN values transformations:
Implemented transformations to handle NAN values during data ingestion to ensure data quality.
<img width="951" alt="Transformar NAN values" src="https://github.com/user-attachments/assets/27ea9ab1-ed13-488a-8d86-b12b80c7a0b8">


## Example of "Total Trade Volume per Year" query:
Showcased an example query that aggregates total trading volume by year for analysis.
<img width="426" alt="EXAMPLE Total Trade Volume per Year" src="https://github.com/user-attachments/assets/1d01c732-2fb4-4706-958e-a742fb18441d">


## Execution of commands directly from the shell:
Executed a .sql file that automates table generation and data processing. (Execute transform_and_export_parquet.sql)
<img width="943" alt="EJECUTAR COMANDOS" src="https://github.com/user-attachments/assets/bbbc36c4-02b6-45d9-90cd-36ba733c3918">


## Example of how to persist data with DuckDB BBDD format:
Illustrated methods for persisting data in DuckDB database format.
<img width="956" alt="Persist Data" src="https://github.com/user-attachments/assets/5dab75c8-b9df-4b0f-954d-91d0e69ae014">


## Example of automatitation of data process using python scripts:
Demonstrated automation techniques utilizing Python scripts for data processing tasks. (Execute main.py)

Need to install requirements first:

<img width="572" alt="requirements" src="https://github.com/user-attachments/assets/37cb885a-b201-4bbe-b203-6427a7e96c30">

python output:
<img width="939" alt="Ejecutar main py" src="https://github.com/user-attachments/assets/d048a104-7993-42cd-8814-a3057324609d">

