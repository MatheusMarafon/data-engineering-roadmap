from airflow.decorators import dag, task
from airflow.models import Variable
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime, timedelta
import logging # Para melhorar os logs

# 1. Configurando Retries (Resiliência)
default_args = {
    'owner': 'Matheus',
    'retries': 3, # Tenta de novo 3 vezes antes de marcar como falha
    'retry_delay': timedelta(minutes=5), # Espera 5 min entre tentativas
}

@dag(
    dag_id="etl_batch_final_resiliente",
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md="""
    ### DAG de Processamento de Vendas (Semana 09)
    Esta DAG realiza o ETL de vendas diárias:
    - **Cria** a tabela no Postgres se não existir.
    - **Extrai** o nome da partição baseado na data.
    - **Transforma** simulando limpeza de dados.
    - **Carrega** metadados no Postgres.
    """, # Docstring que aparece na UI do Airflow
    tags=["producao", "resiliencia"],
)
def etl_pipeline_final():

    criar_tabela = SQLExecuteQueryOperator(
        task_id="criar_tabela_vendas",
        conn_id="postgres_db",
        sql="""
            CREATE TABLE IF NOT EXISTS vendas_processadas (
                id SERIAL PRIMARY KEY,
                nome_arquivo VARCHAR(255),
                data_processamento TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
    )

    @task
    def extrair_particao():
        # Melhorando logs
        logging.info("Iniciando processo de extração de variáveis.")
        caminho = Variable.get("caminho_saida_etl")
        nome_arquivo = f"dados_vendas_{datetime.now().strftime('%Y%m%d')}.csv"
        logging.info(f"Arquivo identificado: {nome_arquivo} no caminho: {caminho}")
        return nome_arquivo 

    @task
    def transformar_particao(arquivo: str):
        """Simula a transformação e limpeza de dados."""
        logging.info(f"Limpando o ficheiro {arquivo}...")
        # Simulação de erro aleatório para testar o Retry (opcional para teste)
        # if datetime.now().second % 2 == 0: raise ValueError("Erro simulado!")
        return {"arquivo": arquivo, "status": "transformado"}

    @task
    def carregar_no_postgres(resultado: dict):
        logging.info(f"Finalizando carga do ficheiro {resultado['arquivo']} no Postgres.")

    # Fluxo
    arquivo = extrair_particao()
    criar_tabela >> arquivo
    processado = transformar_particao(arquivo)
    carregar_no_postgres(processado)

etl_pipeline_final()