The 'Pipeline' activity within Microsoft Fabric is an orchestration tool that allows you to place all the activities performed within the workspace to deploy the pipeline and run all the activities.

Explanation of each activity:

- **ForEach Activity**: This Activity allows you to read the created parameter ''tables_names'' which is an array with all the names of the source tables, and it will iterate over each one of them.
  
- **Copy_Data activity**: this activity is inside the For_Each, this activity's main feature is to copy the data from the Source ''Kaggle_staging'' to the ''Bronze_Layer'' without any type of transformations.
The idea of ​​having the copy data inside a for each is to allow a dynamic iteration to copy all the tables from the Source to the bronze layer, one by one, without having to do multiple copy_data.

- **Notebook Activity**: this activity allows us to place the notebook we want to run inside it, so when the activity is launched it will run the notebook that will be associated (eg Notebook Activity ''Transformations'' will run the Notebook ''TransformationsSilver'')

- **E-mail Activity**: This activity's main feature is to help control the pipeline flow. If something goes wrong in any of the activities, an email will be sent to say what error occurred during the pipeline.

  <img width="1911" alt="image" src="https://github.com/user-attachments/assets/19be7679-8590-4e4e-b2ca-7e1281441f90" />
