I chose Microsoft Fabric to perform data integration in my project because of its robustness and efficient integration of several tools required to implement a modern OLAP system. 
Microsoft Fabric offers a complete set of solutions that facilitate the processing of large volumes of data, automation of pipelines, and integration of visualizations, which perfectly fits with the objectives of my project.

**LakeHouses Why?**

One of the main components of Microsoft Fabric is the lakehouse architecture.
Lakehouse is a solution that combines the best elements of data lakes and data warehouses. It offers the flexibility of storing raw data in a data lake format, but also allows for  analytical and operational queries, as if it were a data warehouse.
This facilitates the processing of data from multiple sources, providing an ideal environment for large volumes of structured and unstructured data.

In this project, I used the Lakehouse architecture to consolidate data from different sources and transform this information efficiently, creating a medallion architecture (Bronze, Silver, Gold)

**Integrated Power BI**

Another great advantage of Microsoft Fabric is the direct integration with Power BI, which is a powerful data visualization tool. 
By integrating Power BI with Microsoft Fabric, I was able to create dynamic dashboards and reports that provide insights to stakeholders to visualize the analyses in a clear and interactive way.

Power BI was used to generate visualizations of data from the OLAP system, facilitating the analysis of the results obtained with the ETL processes and the processing of large volumes of data.

**Data Pipelines within Microsoft Fabric**

Microsoft Fabric also offers a set of pipelines that help automate the data ingestion, transformation, and loading (ETL) process. With pipelines, I was able to set up automated data flows to ensure that data from external systems, in this case ''kaggle_staging'' which is an OLTP system on an on-premises server in Sql Server. This allowed the data to be extracted, transformed and loaded into the OLAP system developed in Fabric.

These pipelines made the data integration process much more efficient and scalable, in addition to allowing me to automate repetitive tasks, reducing the risk of errors and optimizing processing time.

**OLAP system in Microsoft Fabric**

The main idea of ​​my project was to read data from the external OLAP system, called "kaggle_staging", and create an OLAP system within Microsoft Fabric. This involved using features such as lakehouse and pipelines to process and organize the data, ensuring that it was ready for analysis. Using Microsoft Fabric allowed me to create a more agile and flexible OLAP system, taking advantage of the native integration with Power BI to facilitate the visualization and exploration of data interactively.
