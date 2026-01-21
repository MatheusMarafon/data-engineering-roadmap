from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import boto3
import os

# CONFIGURAÇÕES
# Troque pelo nome exato do seu bucket criado na terça/quarta
BUCKET_NAME = "matheus-data-lake-semana11"
LOCAL_FILE_PATH = "/opt/airflow/dags/usuarios.csv"  # Arquivo gerado anteriormente


def upload_partitioned():
    # 1. Configurar o cliente S3 (Boto3 busca credenciais do ambiente/Airflow)
    s3 = boto3.client("s3")

    # 2. Definir a estrutura de partição baseada na data de hoje (Execução)
    now = datetime.now()
    partition_path = (
        f"processed/{now.year}/{now.month:02d}/{now.day:02d}/usuarios_status.csv"
    )

    # 3. Verificar se o arquivo existe antes de subir
    if not os.path.exists(LOCAL_FILE_PATH):
        raise FileNotFoundError(f"Arquivo não encontrado: {LOCAL_FILE_PATH}")

    # 4. Upload
    print(f"Iniciando upload para: s3://{BUCKET_NAME}/{partition_path}")
    s3.upload_file(LOCAL_FILE_PATH, BUCKET_NAME, partition_path)
    print("Upload com sucesso!")


with DAG(
    "s3_partitioned_upload",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["week_11", "s3", "boto3"],
) as dag:

    upload_task = PythonOperator(
        task_id="upload_to_s3_partitioned", python_callable=upload_partitioned
    )
