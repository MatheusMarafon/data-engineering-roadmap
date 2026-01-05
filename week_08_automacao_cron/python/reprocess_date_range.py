import argparse
from datetime import datetime, timedelta
from etl import run_etl

def run_backfill(source_path, start_date, end_date, is_debug):
    """ Funcao que itera sobre um intervalo de datas e roda o ETL para cada dia """
    # Converte strings para objetos de data
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    current_date = start
    print(f"INICIANDO REPROCESSAMENTO DE {start_date} ATE {end_date}")

    # Loop: enquanto a data atual for menor ou igual a data final
    while current_date <= end:
        date_str = current_date.strftime('%Y-%m-%d')
        print(f"\n[>>>] Processando data: {date_str}")

        # Chama a funcao run_etl do arquivo etl.py otiginal
        # Isso garante que vamos usar a memsa lógica, sem duplicar o codigo
        run_etl(source_path, date_str, is_debug)

        # Avanca um dia
        current_date += timedelta(days=1)

    print("\n REPROCESSAMENTO CONCLUIDO!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script de Reprocessamento (Backfill)")

    parser.add_argument("--source", required=True, help="Caminho do arquivo CSV")
    parser.add_argument("--start", required=True, help="Data de inicio (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="Data de fim (YYYY-MM-DD)")
    parser.add_argument("--debug", action="store_true", help="Modo Debug")

    args = parser.parse_args()
    run_backfill(args.source, args.start, args.end, args.debug)
