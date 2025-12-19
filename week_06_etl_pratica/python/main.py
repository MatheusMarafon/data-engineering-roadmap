import argparse
import time

# Importando funções a serem chamadas
from extract import ler_dados_vendas, buscar_cotacoes
from transform import process_data
from load import carregar_dados

''
def run_pipeline(caminho_arquivo):
    start_time = time.time()
    print("-------------------------------")
    print(" INICIANDO PIPELINE DE VENDAS ")
    print("-------------------------------")

    try:
        # Extract
        print("\n[1/3] EXTRACT: Coletando dados...")
        df_raw = ler_dados_vendas(caminho_arquivo)
        cotacoes = buscar_cotacoes()

        # Transform
        print("\n[2/3] TRANSFORM: Limpando e calculando...")
        df_clean = process_data(df_raw, cotacoes)

        # Load
        print("\n[3/3] LOAD: Salvando no PostgreSQL...")
        carregar_dados(df_clean)

        print("----------------------------------")
        print(" PIPELINE CONCLUÍDO COM SUCESSO! ")
        print(f"Tempo Total: {start_time}")
        print("----------------------------------")

    except Exception as e:
        print("\n Erro fatal no pipeline:")
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pipeline ETL de Vendas Internacionais"
    )
    parser.add_argument(
        "--arquivo", type=str, required=True, help="Caminho do CSV de vendas"
    )
    args = parser.parse_args()

    run_pipeline(args.arquivo)
