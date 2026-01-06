from airflow.decorators import dag, task
from airflow.models import Variable
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime
import time

@dag(
    dag_id="etl_batch_quinta_feira",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["semana_09", "quinta_feira"],
)
def etl_pipeline_dinamico():

    # 1. Tarefa para criar a tabela (Usando a Connection que você criou via CLI)
    criar_tabela_vendas = SQLExecuteQueryOperator(
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
        caminho = Variable.get("caminho_saida_etl")
        print(f"Buscando arquivos no diretório: {caminho}")
        nome_arquivo = f"dados_vendas_{datetime.now().strftime('%Y%m%d')}.csv"
        return nome_arquivo 

    @task
    def transformar_particao(arquivo_recebido: str):
        print(f"Iniciando limpeza do arquivo: {arquivo_recebido}")
        time.sleep(2)
        return {"arquivo": arquivo_recebido, "status": "sucesso"}

    @task
    def carregar_no_postgres(resultado_transformado: dict):
        print(f"Carregando {resultado_transformado['arquivo']} no banco...")

    # Definindo a nova ordem: Criar tabela PRIMEIRO, depois o resto
    fluxo_extrair = extrair_particao()
    # Aqui fazemos a dependência: criar_tabela deve rodar antes de extrair
    criar_tabela_vendas >> fluxo_extrair 
    
    resultado = transformar_particao(fluxo_extrair)
    carregar_no_postgres(resultado)

etl_pipeline_dinamico()