This Lakehouse built on Fabric is a useful technology since it combines data lakes with data warehouses. We can load any type of files, including files and tables in tabular format with delta table format.

The delta format tables in this lakehouse come from the OLTP system ''Kaggle_staging'' in raw format. It is useful to have a layer without any type of transformation to understand how the data comes from the source. This is exactly the idea behind this bronze lakehouse.

Lakehouses in Microsoft Fabric are powerful since they offer the organization of tables in Delta format in ''Tables''. We can have any type of unstructured file that will be in the ''Files'' folder of the lakehouse. This layer also offers a SQL endpoint Datawarehouse for SQL queries.

The structure of this lakehouse after the tables are loaded in delta format is as follows:

<img width="1909" alt="image" src="https://github.com/user-attachments/assets/a1c7852f-0ac5-4f01-b3c2-782103fd693f" />
