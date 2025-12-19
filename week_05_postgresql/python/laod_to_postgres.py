import pandas as pd
from sqlalchemy import create_engine
import os

#Configuração do banco
db_user = 'postgres'
db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'
db_pass = '' #Vazio pois o bd não tem senha


#Testa as duas url's (com e sem senha)
if db_pass:
    database_url = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
else:
    database_url = f"postgresql://{db_user}@{db_host}:{db_port}/{db_name}"


def carregar_dados():
    print("Iniciando integração Python -> PostgreSQL...")
    #Tentando conexão com o db
    try:
        engine = create_engine(database_url)
        with engine.connect() as conn:
            print("Conexão com o banco estabelecida com sucesso!")
    except Exception as e:
        print(f"Erro fatal ao conectao no banco. Verifique se o PostgreSQL está ligado. \nDetalhe: {e}")
        return
    
    #Arquivo a ser lido
    arquivo_csv = 'processed/vendas_semana.csv'

    #Verifica se o arquivo existe
    if not os.path.exists(arquivo_csv):
        print(f"Arquivo {arquivo_csv} não foi encontrado.")
        print("Criando dados de teste na memória para não travar o script...")

        #Criamos dados falsos para teste
        data = {
            'vendedor': ['Teste_Python', 'Teste_Python'],
            'categoria': ['Auto', 'Auto'],
            'valor': [100.50, 200.00]
        }
        df = pd.DataFrame(data)
    else:
        print(f"Lendo arquivo: {arquivo_csv}")
        df = pd.read_csv(arquivo_csv)

    print(f"Enviando {len(df)} linhas para a tabela 'vendas_importadas'...")

    try:
        df.to_sql('vendas_importadas', engine, if_exists='replace', index=False)
        print("SUCESSO! Dados carregados. Confira no DBeaver.")
    except Exception as e:
        print(f"Erro ao salvar a tabela: {e}")
    
if __name__ == '__main__':
    carregar_dados()