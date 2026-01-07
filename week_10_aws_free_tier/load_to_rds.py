import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Configurações de URL
DATABASE_URL = f"postgresql+psycopg2://{os.getenv('RDS_USER')}:{os.getenv('RDS_PASSWORD')}@{os.getenv('RDS_HOST')}:{os.getenv('RDS_PORT')}/{os.getenv('RDS_DB_NAME')}"


def load_data_to_rds(csv_path, table_name):
    try:
        # Criar motor de conexão
        engine = create_engine(DATABASE_URL)

        # Ler os dados
        df = pd.read_csv(csv_path)
        print(f"Arquivo {csv_path} lido com sucesso!")

        # Carregar para o RDS
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Dados carregados da tabela '{table_name}' no RDS!")

    except Exception as e:
        print(f"Erro ao carregar: {e}")


if __name__ == "__main__":
    # Cria um csv caso não tenha
    teste_df = pd.DataFrame(
        {
            "id": [1, 2],
            "nome": ["Matheus", "Engenharia"],
            "data": ["2026-01-07", "2026-01-08"],
        }
    )
    teste_df.to_csv("dados_processados.csv", index=False)

    # Executa o carregamento
    load_data_to_rds("dados_processados.csv", "tb_processada")
