This Gold Layer is also a lakehouse, but with a different purpose. In Bronze, the idea was to have the data in raw format, while in Silver, the idea was to have the data transformed.

This layer is used to store the data already aggregated and prepared with the ''Data_Modeling'' notebook, which prepares the entire Star Schema data model. This notebook contains the Silver data and performs the aggregations and joins necessary to create the dimension and fact tables that will be loaded into this layer.

This is the Layer that will serve as the EndPoint for the Report in BI.

<img width="1906" alt="image" src="https://github.com/user-attachments/assets/9cfaa681-913f-4ec6-9e99-4edf4956ef6a" />
