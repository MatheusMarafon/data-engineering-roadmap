from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import pandas as pd

def upload_to_rds():
    # Lendo o arquivo que geramos na terça 
    file_path = '/opt/airflow/dags/usuarios.csv'
    df = pd.read_csv(file_path)
    
    # Criando a conexão via Hook
    # Lembre-se: você deve criar a conexão 'postgres_rds' no Airflow UI
    pg_hook = PostgresHook(postgres_conn_id='postgres_rds')
    
    # Usando SQLAlchemy para inserir os dados de forma eficiente
    engine = pg_hook.get_sqlalchemy_engine()
    
    print("Iniciando carga no RDS matheus-db-semana10")
    df.to_sql('tb_usuarios_monitorados', engine, if_exists='replace', index=False)
    print("Carga finalizada com sucesso!")

with DAG(
    'etl_to_rds',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=['week_11', 'aws', 'rds']
) as dag:

    load_data = PythonOperator(
        task_id='load_to_rds_task',
        python_callable=upload_to_rds
    )