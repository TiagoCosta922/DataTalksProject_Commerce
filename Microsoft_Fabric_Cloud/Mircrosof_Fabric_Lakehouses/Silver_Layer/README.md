As explained in the Bronze layer's ''Readme'', this is also a lakehouse but with a different purpose, since the purpose of the bronze layer was to have all the data loaded from the ''kaggle_staging'' OLTP system.

This layer is intended to have all the tables with the transformations performed through the ''TransformationSilver'' notebook that reads the delta tables from the bronze layer, performs the transformations and loads them into this Silver Layer, already with the transformations.

We can analyze the data like this, with the data already cleaned and standardized.

<img width="1898" alt="image" src="https://github.com/user-attachments/assets/e857f0f6-6a65-4ce0-b4d1-cece9e4956d0" />
