from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def dizer_ola():
    print("Ola Airflow! Agora vai!")

def dizer_fim():
    print("Pipeline finalizado.")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='hello_world_tutorial',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule='@daily',   # <--- AQUI MUDOU (era schedule_interval)
    catchup=False
) as dag:

    task_ola = PythonOperator(
        task_id='print_ola',
        python_callable=dizer_ola
    )

    task_fim = PythonOperator(
        task_id='print_fim',
        python_callable=dizer_fim
    )

    task_ola >> task_fim