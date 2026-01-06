from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import time

# Funções das etapas do ETL
def extract():
    print("Iniciando Extração...")
    time.sleep(2)
    print("Dados extraídos com sucesso!")

def transform():
    print("Iniciando Transformação...")
    time.sleep(2)
    print("Dados transformados (limpeza e agregação concluídas).")

def load():
    print("Iniciando Carga...")
    time.sleep(2)
    print("Dados carregados no Data Warehouse!")

# Configurações
default_args = { 
    'owner': 'Matheus',
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

# Definição da DAG
with DAG(
    dag_id='etl_batch_process',
    default_args=default_args,
    description='Pipeline de ETL simulando Extract, Transform e Load',
    start_date=datetime(2026, 1, 1),
    schedule='@daily', 
    catchup=False,
    tags=['eng_dados', 'batch']
) as dag:    

    # Definindo as Tasks
    task_extract = PythonOperator(
        task_id='extrair_dados',
        python_callable=extract
    )

    task_transform = PythonOperator(
        task_id='transformar_dados',
        python_callable=transform
    )

    task_load = PythonOperator(
        task_id='carregar_dados',
        python_callable=load
    )

    # Fluxo do pipeline
    task_extract >> task_transform >> task_load