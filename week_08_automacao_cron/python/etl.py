import argparse
import os
import pandas as pd
import logging
from datetime import datetime
from dotenv import load_dotenv

# Carrega variaveis do arquivo .env
load_dotenv()

# CONFIGURACAO DE LOGGING
# Cria a pasta 'logs' no nivel acima da pasta 'python'
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Define o arquivo de log: logs/etl.log
LOG_FILE = os.path.join(LOG_DIR, "etl.log")

# Configura o logger para escrever no arquivo E na tela
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(
            LOG_FILE, mode="a", encoding="utf-8"
        ),  # Salva no arquivo (append)
        logging.StreamHandler(),  # Mostra na tela
    ],
)


def run_etl(source_path, run_date, is_debug):
    """
    Funcao principal que simula o ETL com logging.
    """
    # Se for debug, muda o nivel do log para mostrar tudo
    if is_debug:
        logging.getLogger().setLevel(logging.DEBUG)

    logging.info("-" * 40)
    logging.info(f"INICIANDO ETL | Data de processamento: {run_date}")
    logging.info("-" * 40)

    # Verifica credenciais
    db_user = os.getenv("DB_USER")
    logging.debug(f"Usuario do banco carregado do .env: {db_user}")

    # EXTRACTION
    if not os.path.exists(source_path):
        logging.error(f"Arquivo nao encontrado: {source_path}")
        return

    try:
        logging.info(f"Lendo arquivo: {source_path}")
        df = pd.read_csv(source_path)

        # TRANSFORMATION
        df["data_processamento"] = run_date
        logging.info(f"Transformacao concluida. Linhas processadas: {len(df)}")

        # LOAD
        output_folder = os.getenv("OUTPUT_FOLDER", "./output")
        os.makedirs(output_folder, exist_ok=True)

        filename = f"processed_{run_date}_{os.path.basename(source_path)}"
        output_path = os.path.join(output_folder, filename)

        df.to_csv(output_path, index=False)
        logging.info(f"Arquivo salvo com sucesso em: {output_path}")

    except Exception as e:
        logging.error(f"Falha no processamento: {e}", exc_info=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script de ETL com Logging")

    parser.add_argument("--source", required=True, help="Caminho do arquivo CSV")
    parser.add_argument(
        "--date", required=False, default=datetime.now().strftime("%Y-%m-%d")
    )
    parser.add_argument("--debug", action="store_true", help="Ativa logs de debug")

    args = parser.parse_args()

    run_etl(args.source, args.date, args.debug)
