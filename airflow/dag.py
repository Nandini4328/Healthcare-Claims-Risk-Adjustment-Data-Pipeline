from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from processing.transform import transform_data

def run_pipeline():
    df = transform_data("data/sample_claims.json")
    print(df.head())

with DAG(
    dag_id="healthcare_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    task = PythonOperator(
        task_id="transform_task",
        python_callable=run_pipeline
    )
