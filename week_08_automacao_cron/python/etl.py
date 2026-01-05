import argparse
import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def run_etl(source_path, run_date, is_debug):
    """ " Função que simula o ETL. Recebe parametros vindos da linha de comando"""
    print("-" * 40)
    print(f"INICIANDO ELT | Data de processamento: {run_date}")
    print("-" * 40)

    # Verifica credenciais (provando que o .env funcionou)
    db_user = os.getenv("DB_USER")
    if is_debug:
        print(f"[DEBUG] Usuario do banco carregado do .env: {db_user}")

    # Extração
    if not os.path.exists(source_path):
        print(f"[ERRO] Arquivo nao encontrado: {source_path}")
        return
    try:
        print(f"[INFO] Lendo arquivo: {source_path}")
        df = pd.read_csv(source_path)

        # Transformação
        # Adicionando uma coluna de metadata para simulação
        df["data_processamento"] = run_date
        print(f"[INFO] Transformacao concluida. Linhas processadas: {len(df)}")

        # Carregamento (salvar na pasta de saida configurada no .env)
        output_folder = os.getenv("OUTPUT_FOLDER", "./output")
        os.makedirs(output_folder, exist_ok=True)

        filename = f"processed_{run_date}_{os.path.basename(source_path)}"
        output_path = os.path.join(output_folder, filename)

        df.to_csv(output_path, index=False)
        print(f"[SUCESSO] Arquivo salvo em: {output_path}")

    except Exception as e:
        print(f"[ERRO] Falha no processamento: {e}")


if __name__ == "__main__":
    # Configuracao do CLI
    parser = argparse.ArgumentParser(description="Script de ETL Parametrizavel")

    # Argumento obrigatorio: caminho do arquivo
    parser.add_argument(
        "--source", required=True, help="Caminho do arquivo CSV de entrada"
    )

    # Argumento opcional: data de ref (se nao passar, pega hoje)
    parser.add_argument(
        "--date",
        required=False,
        default=datetime.now().strftime("%Y-%m-%d"),
        help="Data de referencia para processamento (YYYY-MM-DD)",
    )

    # Argumento FLAG (True/False): Modo degub
    parser.add_argument("--debug", action="store_true", help="Ativa logs detalhados")

    # Le os argumentos passados no terminal
    args = parser.parse_args()

    # Chama a funcao principal passando os argumentos
    run_etl(args.source, args.date, args.debug)
