# Code Explanation

This folder is intended for scripts with pyspark within microsoft fabric, using notebooks.

## Lakehouses_ABFS_Path

The 'Lakehouses_ABFS_Path' file was created with the purpose of helping any other notebooks that were created to pass the ABFS_Path path of the lakehouse dynamically,
without having to constantly copy the path when we want to read or write delta tables in the lakehouses.

## TransformationSilver

This Notebook is used to load all delta tables in bronze in raw format, 
make the necessary transformations to the data to maintain their integrity and uniformity, and load the delta tables already transformed into silver layer.

A date record called 'RegistrationDate' column was created that will be used to create partitions. Whenever new data is inserted to be processed, we will know the date of the transformations.


## Data_Modeling

This notebook is used to model data. The Star Schema data model was chosen. 

The data will be loaded from silver and the necessary table aggregations and joins will be made to create the dimension tables and the fact table. 

The data model will be as shown in the following image:


