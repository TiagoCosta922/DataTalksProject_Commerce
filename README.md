# DataTalksProject_Commerce


## NOTE IMPORTANT: In each folder there will be images about the process and a more detailed explanation of each point. Please open the folders (e.g. inside the scripts there will be an explanation of what was done and why)



## DataSet 

### OverView

the Grocery Sales Database (Source Kaggle):

Sales: This includes data about individual sales, such as the products purchased, quantities, prices, and total sales.

Customer: Contains information about customers such as their Name, location, etc.

Product: This includes information about the products sold, such as product names, categories, prices, etc.

Employee: Includes details about employees involved in the sales process, such as their names, location, etc. 

Geographical Information: Data about the locations of stores, cities, and countries.


Source :

Kaggle : https://www.kaggle.com/datasets/andrexibiza/grocery-sales-dataset

Size it is small aprox. 500MB.



## Project Architecture

The entire process of this project is designed around data extraction using the Kaggle API to load data into an OLTP system, which will be called the "Kaggle" Database. Data extraction will be handled via Python, orchestrated by Prefect, and the data manipulation will occur daily.

Once loaded into the OLTP system, the data from the "Kaggle" Database will be transferred to a secondary database on the same server, referred to as "Kaggle_Staging." The purpose of this staging area is to support OLAP processes, and data will be copied from the "Kaggle" Database to the "Kaggle_Staging" Database once a day to prevent overloading the transactional database.

The "Kaggle_Staging" database will serve as the foundation for analytical work, using Microsoft technologies available in Microsoft Fabric.

Microsoft Fabric will act as the OLAP system. We will implement Medallion architecture, with the data in the "Kaggle_Staging" database initially loaded into a lakehouse known as the "Bronze_Layer" in its raw form. Subsequently, Spark-based transformations will be performed using notebooks in Microsoft Fabric, and the transformed data will be loaded into the "Silver_Layer." In the "Gold_Layer," all aggregations will be completed, and a Star Schema model will be used for data modeling. This structured approach will enable the creation of reports for analysis with Power BI. Microsoft Fabric was selected for this project due to its unified platform, which integrates multiple services, streamlining the entire process and providing a solid foundation for future scalability.

The entire process in Microsoft Fabric will be managed via a pipeline.

## Technologies
This project adopts a hybrid approach, combining on-premises technologies with cloud solutions, specifically leveraging:

- SQL Server: For local data storage.
- Prefect: For orchestrating the data extraction flows, loading data into the "Kaggle" Database, and copying data to the staging area ("Kaggle_Staging").
- Spark: For data processing and transformation.
- Microsoft Fabric: For notebooks, lakehouses, pipelines, and Power BI integration.

The entire process is illustrated in the following image:


<img width="898" alt="image" src="https://github.com/user-attachments/assets/4f74ea79-a375-4b74-a8c6-1d29a2dd49cc" />




## Report

### Analysis Quantity Sales

<img width="1275" alt="image" src="https://github.com/user-attachments/assets/c92e1362-c526-4559-9df1-484fe9473b7e" />

### Analysis Total Price Sales

<img width="1280" alt="image" src="https://github.com/user-attachments/assets/8085709f-26a3-4388-aca1-fa89fd85e666" />





