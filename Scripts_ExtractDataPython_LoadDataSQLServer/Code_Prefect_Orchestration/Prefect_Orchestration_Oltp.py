from prefect import task, flow
from prefect.schedules import Interval
from datetime import timedelta, datetime
from Extract_Data.Extract_Data import extract_data
from Load_Data.Load_Data import main


@task
def extract_task():
    extract_data()
    print("Data extraction completed.")

@task
def load_task():
    main()
    print("Data loading completed.")

@flow()
def Load_Data_OLTP():
    extract_task()
    load_task()

if __name__ == "__main__":
    Load_Data_OLTP.serve(
        name="Extract Data and Load into OLTP",
        schedule=Interval(
            timedelta(days=1),  
            anchor_date=datetime(2025, 3, 16, 0, 0),  
            timezone="Europe/Lisbon"  
        )
    )

