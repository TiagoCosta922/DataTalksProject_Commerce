Nesta pasta estão todos os Scripts usados com python:

**O que foi desenvolvido?**


**Folder ''Code_Copy_Data_kaggle_to_kaggle_staging''**

The **''Code_Copy_Data_kaggle_to_kaggle_staging''** folder contains a python code that connects to the on-premises SQL Server database, and copies the entire data from the **''Kaggle''** database to the **''Kaggle_staging''** database.

<img width="505" alt="image" src="https://github.com/user-attachments/assets/a07ec36c-7be7-438d-ab47-db57df35f8da" />

**Porque que o staging é importante?**

We should not read data directly from OLTP systems for analysis, we can make the entire transactional system slow, for this it is a good practice to make a full copy of the data for staging, this staging area will be used for the OLAP system in Microsoft Fabric.




**Folder ''Code_Extract_Data_kaggle''**

This folder contains a python code that does all the data extraction through the Kaggle API and places all the csv files on the local server, in the files.

It contains a file ''__init__.py'' to say that this folder is a python module so that we can use the functions inside the .py files in this folder in the future.




**Folder ''Code_Load_Data_To_OLTP''**

This folder contains the python files that connect to the database and insert the CSV files that were extracted from the Kaggle API and load them into the SQL Server OLTP system in tabular format.

It contains a file ''__init__.py'' to indicate that this folder is a python module so that we can use the functions within the .py files in this folder in the future.




**Foler ''Prefect_Orchestratiom''**

In this folder we have two python files:

- The file **''Prefect_Orchestration_Oltp''** orchestrates the files **''Extract_Data''** inside the folder **''Code_Extract_Data_kaggle''** and the file **''Load_Data''** inside the folder **''Code_Load_Data_To_OLTP''**. This flow will occur every day, once a day.

- The file **''Prefect_Orchestration_Olap''** orchestrates the files **''Copy_Data''** inside the folder **''Code_Copy_Data_kaggle_to_kaggle_staging''** . This flow will occur once a month.
