import os
import pyodbc
import pandas as pd
from dotenv import load_dotenv

def copy_data():
    """
    Connects to two SQL Server databases (source and destination), and copies the data 
    from each table in the source database to the destination database.

    The function performs the following steps:
    1. Loads environment variables for SQL Server connection details.
    2. Establishes connections to both the source and destination databases.
    3. Fetches the list of tables from the source database.
    4. For each table:
       - Creates the table in the destination database (with columns as VARCHAR(MAX)).
       - Copies the data from the source table and inserts it into the corresponding table in the destination database.
    5. Commits the changes to the destination database.
    6. Closes the connections to both databases after the process is complete.

    Exception handling is included to catch and display any errors during the process.
    """
    load_dotenv()

    server = os.getenv('SQL_SERVER')
    database = os.getenv('SQL_DATABASE')
    database_destino = os.getenv('SQL_DATABASE_DESTINATION')
    username = os.getenv('SQL_USERNAME') 
    password = os.getenv('SQL_PASSWORD')  

    # Connection strings for source and destination databases
    connection_string_origem = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    connection_string_destino = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database_destino};UID={username};PWD={password}'

    try:
        conn_origem = pyodbc.connect(connection_string_origem)
        print("Connected to the source database")


        conn_destino = pyodbc.connect(connection_string_destino)
        print("Connected to the destination database")

        cursor_origem = conn_origem.cursor()
        cursor_destino = conn_destino.cursor()

        # Fetch the list of tables from the source database
        cursor_origem.execute("SELECT table_name FROM information_schema.tables WHERE table_type = 'BASE TABLE'")
        tabelas = cursor_origem.fetchall()

        for tabela in tabelas:
            tabela_nome = tabela[0]
            print(f"Copying table: {tabela_nome}")

            # Get the structure of the table from the source (without data)
            cursor_origem.execute(f"SELECT * FROM {tabela_nome} WHERE 1=0") 
            colunas = [col[0] for col in cursor_origem.description]  # Get column names
            colunas_str = ", ".join(colunas)

            # Create the table in the destination database (with columns as VARCHAR(MAX))
            create_table_query = f"CREATE TABLE {tabela_nome} ({', '.join([f'{col} VARCHAR(MAX)' for col in colunas])})"
            cursor_destino.execute(create_table_query)
            
            # Fetch data from the source table
            cursor_origem.execute(f"SELECT * FROM {tabela_nome}")
            rows = cursor_origem.fetchall()

            # Insert data into the destination table
            for row in rows:
                placeholders = ", ".join(["?"] * len(row))
                insert_query = f"INSERT INTO {tabela_nome} ({colunas_str}) VALUES ({placeholders})"
                cursor_destino.execute(insert_query, row)

        conn_destino.commit()

        print("Table copy completed successfully!")

    except Exception as e:
        print(f"Error during data copy: {e}")
    finally:
        if conn_origem:
            conn_origem.close()
        if conn_destino:
            conn_destino.close()

copy_data()
