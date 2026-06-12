from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# ── Dummy imports (replace with your actual module functions later) ──
def extract_stripe():
    print("Extracting data from Stripe API...")

def extract_salesforce():
    print("Extracting data from Salesforce API...")

def extract_zendesk():
    print("Extracting data from Zendesk API...")

def transform_data():
    print("Cleaning nulls, standardizing dates/currency, mapping to unified schema...")

def load_to_warehouse():
    print("Upserting data into PostgreSQL/Snowflake via SQLAlchemy...")

def upload_to_s3():
    print("Writing raw JSON to AWS S3 intermediate data lake...")

# ── Default settings for all tasks ──
default_args = {
    "owner": "Kamalesh",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": True,
    "email": ["kamaleshsuresh2008@gmail.com"]
}

# ── Define the DAG ──
with DAG(
    dag_id="enterprise_etl_pipeline",
    description="Extract from Stripe, Salesforce, Zendesk → Transform → Load to Data Warehouse",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    default_args=default_args,
    tags=["etl", "warehouse", "production"]
) as dag:

    # EXTRACTION TASKS
    extract_stripe_task = PythonOperator(
        task_id="extract_stripe",
        python_callable=extract_stripe
    )

    extract_salesforce_task = PythonOperator(
        task_id="extract_salesforce",
        python_callable=extract_salesforce
    )

    extract_zendesk_task = PythonOperator(
        task_id="extract_zendesk",
        python_callable=extract_zendesk
    )

    # S3 UPLOAD (after extraction)
    upload_s3_task = PythonOperator(
        task_id="upload_raw_to_s3",
        python_callable=upload_to_s3
    )

    # TRANSFORMATION TASK
    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    # LOAD TASK
    load_task = PythonOperator(
        task_id="load_to_warehouse",
        python_callable=load_to_warehouse
    )

    # ── Pipeline Order ──
    # Extract all 3 sources in parallel → upload to S3 → transform → load
    [extract_stripe_task, extract_salesforce_task, extract_zendesk_task] >> upload_s3_task >> transform_task >> load_task