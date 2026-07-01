from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "Kamalesh",
    "retries": 1,
    "email_on_failure": True,
    "email": ["kamaleshsuresh2008@gmail.com"],  
}

with DAG(
    dag_id="zaalima_main_pipeline",
    description="Automated trigger for the Zaalima ETL pipeline",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args=default_args,
) as dag:

    run_main_pipeline = BashOperator(
        task_id="execute_main_py",
        bash_command="python C:/Users/Admin/zaalima_etl/main.py"
    )

    run_main_pipeline