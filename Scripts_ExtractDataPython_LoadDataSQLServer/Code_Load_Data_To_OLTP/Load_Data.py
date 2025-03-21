import os
import pyodbc
import pandas as pd
from dotenv import load_dotenv

def connect():
    """
    Establishes a connection to the SQL Server database using the credentials defined in the .env file.
    
    The function loads the environment variables using `dotenv`, reads the server and database details,
    and tries to establish a connection using `pyodbc`. If successful, it returns the connection object.
    If an error occurs during the connection attempt, it prints the error and returns `None`.

    Returns:
        pyodbc.Connection: A connection object to the SQL Server database if the connection is successful.
        None: If the connection fails.
        
    Example:
        conn = connect()
        if conn:
            # proceed with database operations
        else:
            # handle connection error
    """
    load_dotenv()

    server = os.getenv('SQL_SERVER')
    database = os.getenv('SQL_DATABASE')
    username = os.getenv('SQL_USERNAME')  # Usuário SQL Server
    password = os.getenv('SQL_PASSWORD')  # Senha do usuário SQL Server

    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        conn = pyodbc.connect(connection_string)
        print("Connected to SQL Server")
        return conn
    except Exception as e:
        print(f"Error with connection: {e}")
        return None

def drop_all_tables(conn):
    """
    Drops all tables from the database if they exist.

    This function queries the `INFORMATION_SCHEMA.TABLES` view to retrieve a list of all table names
    in the database. Then, for each table, it constructs a `DROP TABLE` SQL statement and executes it.
    The connection to the database must be established before this function is called.

    Parameters:
        conn (pyodbc.Connection): The connection object to the SQL Server database.

    Raises:
        Exception: If an error occurs while querying the database or dropping the tables.

    Example:
        drop_all_tables(conn)
    """
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';")
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]
            drop_sql = f"DROP TABLE IF EXISTS {table_name};"
            cursor.execute(drop_sql)
            conn.commit()
            print(f"Table {table_name} dropped successfully!")

    except Exception as e:
        print(f"Error dropping tables: {e}")

def create_table_from_df(conn, df, table_name):
    """
    Creates a new table in the SQL Server database based on the DataFrame columns.
    
    The function dynamically generates a SQL `CREATE TABLE` statement by examining the DataFrame's columns,
    creating each column as `NVARCHAR(MAX)`, which is a flexible data type that can accommodate various types 
    of data, including NULL values. The SQL statement is then executed to create the table in the database.
    
    Parameters:
        conn (pyodbc.Connection): The connection object to the SQL Server database.
        df (pandas.DataFrame): The pandas DataFrame containing the data to create the table. 
                               The column names from the DataFrame will be used as the table column names.
        table_name (str): The name of the table to be created in the database. 
                          This name should not contain spaces or special characters that SQL Server does not allow.
    
    Raises:
        Exception: If there is an error while constructing the SQL query or creating the table in the database.

    Example:
        create_table_from_df(conn, df, "new_table")
    """
    cursor = conn.cursor()
    columns = df.columns
    column_definitions = []
    
    for col in columns:
        column_definitions.append(f"{col} NVARCHAR(MAX)")
    
    create_table_sql = f"CREATE TABLE {table_name} ({', '.join(column_definitions)});"
    try:
        print(f"Creating table {table_name} with columns {', '.join(columns)}")
        cursor.execute(create_table_sql)
        conn.commit()
        print(f"Table {table_name} created successfully!")

    except Exception as e:
        print(f"Error creating table {table_name}: {e}")

def insert_data_into_table(conn, df, table_name):
    """
    Inserts data from a pandas DataFrame into a specified SQL Server table.

    This function iterates over each row of the DataFrame and inserts the data into the corresponding
    SQL Server table using parameterized queries. The rows are inserted one by one, and any NaN or empty
    string values in the DataFrame are replaced with `None` to represent `NULL` values in the database.

    Parameters:
        conn (pyodbc.Connection): The connection object to the SQL Server database.
        df (pandas.DataFrame): The pandas DataFrame containing the data to be inserted into the table.
        table_name (str): The name of the table into which the data will be inserted.

    Raises:
        Exception: If an error occurs during the insertion of data into the table.
    
    Example:
        insert_data_into_table(conn, df, "new_table")
    """
    cursor = conn.cursor()
    columns = df.columns
    values_placeholder = ', '.join(['?'] * len(columns))  # Placeholder for values
    insert_sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values_placeholder})"
    
    try:
        for row in df.itertuples(index=False, name=None):  
            # Replace empty strings and NaN with None (NULL in SQL Server)
            row = [None if pd.isna(value) or value == '' else value for value in row]
            cursor.execute(insert_sql, row)
        
        conn.commit()
        print(f"Data inserted successfully into {table_name}")

    except Exception as e:
        print(f"Error inserting data into {table_name}: {e}")


def load_data_from_csv(folder_path, conn):
    """
    Loads data from all CSV files in a specified folder into SQL Server.

    This function reads each CSV file from the given folder, creates a new table for each file based on
    the file's columns, and inserts the data from the CSV file into the newly created table. Each CSV file's
    name (without the extension) is used as the table name in SQL Server.

    Parameters:
        folder_path (str): The path to the folder containing the CSV files. Each CSV file in the folder will
                           be processed individually.
        conn (pyodbc.Connection): The connection object to the SQL Server database.
    
    Raises:
        Exception: If an error occurs during file reading, table creation, or data insertion for any CSV file.

    Example:
        load_data_from_csv("C:/path/to/csv/folder", conn)
    """
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            table_name = os.path.splitext(filename)[0]  # Table name is the filename without extension

            print(f"Reading file: {filename}")
            
            try:
                # If the file is 'sales.csv', limit the number of rows to 40,000 the file is too large to process so for testing purposes we limit the number of rows to 40,000
                if filename.lower() == 'sales.csv':
                    df = pd.read_csv(file_path, nrows=40000)
                else:
                    df = pd.read_csv(file_path)

                # Create table based on DataFrame columns
                create_table_from_df(conn, df, table_name)

                # Insert data into the table
                insert_data_into_table(conn, df, table_name)

            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
def main():
    """
    Main function that connects to the SQL Server database, drops all existing tables, and loads data from CSV files.

    This function serves as the entry point of the script. It first connects to the SQL Server, then calls
    `drop_all_tables()` to remove all existing tables. Afterward, it processes the CSV files in the specified
    folder and inserts the data into the database.

    Example:
        main()
    """
    conn = connect()

    if conn:
        drop_all_tables(conn)
        folder_path = r'C:\Users\TiagoCosta\Kaggle\data'  # Update with your path to CSV files
        
        load_data_from_csv(folder_path, conn)
    else:
        print("Can't connect to SQL Server")

main()
