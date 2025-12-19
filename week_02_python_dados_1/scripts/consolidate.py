import pandas as pd
import os

def consolidar_csv():
    arquivos_csv = [
        r'C:\Users\matheus.r\Desktop\data-engineering-roadmap\week_02_python_dados\data\raw\vendas.csv',
        r'C:\Users\matheus.r\Desktop\data-engineering-roadmap\week_02_python_dados\data\processed\clean.csv'
    ]
    pasta_saida = r'C:\Users\matheus.r\Desktop\data-engineering-roadmap\week_02_python_dados\data\consolidado'
    arquivo_saida = os.path.join(pasta_saida, 'consolidado.csv')

    dfs = []

    for file_path in arquivos_csv:
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            dfs.append(df)
    if dfs:
        final_df = pd.concat(dfs, ignore_index=True)

        os.makedirs(pasta_saida, exist_ok=True)
        final_df.to_csv(arquivo_saida, index=False)

        print(f"Arquivo salvo em: {arquivo_saida}")
        print(f"Total de linhas: {len(final_df)}")

if __name__ == "__main__":
    consolidar_csv()