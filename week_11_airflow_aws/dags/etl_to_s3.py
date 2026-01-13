from airflow import DAG
from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# CONFIGURAÇÕES 
BUCKET_NAME = "matheus-datalake-semana10"

def transform_data():
    data = "id,nome,status\n1,Matheus,concluido\n2,Airflow,ativo"
    return data

default_args = {
    'owner': 'MatheusMarafon',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'etl_to_s3',
    default_args=default_args,
    description='Semana 11: Task que escreve no S3 após transform',
    schedule_interval=None,
    catchup=False,
    tags=['portfolio', 's3', 'semana11'],
) as dag:

    # Task que simula a lógica de transformação
    transform_step = PythonOperator(
        task_id='transform_data_step',
        python_callable=transform_data
    )

    # Task que faz o Upload para o S3 (Entregável da Terça)
    upload_to_s3 = S3CreateObjectOperator(
        task_id='upload_to_s3_step',
        aws_conn_id='aws_default', 
        s3_bucket=BUCKET_NAME,
        s3_key='transformed_data/usuarios_status.csv',
        data="{{ task_instance.xcom_pull(task_ids='transform_data_step') }}",
        replace=True,
    )

    transform_step >> upload_to_s3