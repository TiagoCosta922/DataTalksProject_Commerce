from prefect import task, flow
from prefect.schedules import Interval
from datetime import timedelta, datetime
from Copy_Data_To_Olap.Copy_Data import copy_data



@task
def copy_data():
    copy_data()
    print("Copy Data from Oltp to Staging Area completed.")

@flow()
def run_copy_data():
    copy_data()
    

run_copy_data.serve(
    name="Copy Data from Oltp to Staging Area",
    schedule=Interval(
        timedelta(days=30),  
        anchor_date=datetime(2025, 3, 16, 0, 0),  
        timezone="Europe/Lisbon"  
    )
)

