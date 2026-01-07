import psycopg2
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()


def test_connection():
    try:
        print("Tentando conectar ao RDS...")
        connection = psycopg2.connect(
            host=os.getenv("RDS_HOST"),
            database=os.getenv("RDS_DB_NAME"),
            user=os.getenv("RDS_USER"),
            password=os.getenv("RDS_PASSWORD"),
            port=os.getenv("RDS_PORT"),
        )

        cursor = connection.cursor()
        # Executa um comando para testar a versão do banco
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print(f"Conexão estabelecida com sucesso!")
        print(f"Versão do Postgres: {record}")

        cursor.close()
        connection.close()
        print("Conexão encerrada com segurança.")

    except Exception as error:
        print(f"Erro ao conectar ao RDS: {error}")


if __name__ == "__main__":
    test_connection()
