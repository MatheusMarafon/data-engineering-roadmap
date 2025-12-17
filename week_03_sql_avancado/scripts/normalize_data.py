import pandas as pd
import json
import os

def normalize_users():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, "data", "raw", "users.json")
    output_dir = os.path.join(base_dir, "data", "processed")
    output_path = os.path.join(output_dir, "api_clean.parquet")

    print(f"Lendo arquivo: {input_path}")
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data=json.load(f)

            #Normaliza os dados aninhados e cria novas colunas
            df = pd.json_normalize(data)

            print(f"Normalização consluída! Shape: {df.shape}")

            #Verificando como ficaram as novas colunas
            print("Colunas geradas(exemplo):")
            print(f"    -{df.columns[0]}")
            print(f"    -{df.columns[-1]}")

            os.makedirs(output_dir, exist_ok=True)

            df.to_parquet(output_path, engine='pyarrow')

            print(f"Arquivo Parquet salvo em: {output_path}")

    except FileNotFoundError:
        print(f"Erro: Arqiuvo {input_path} não encontrado. Rode o script de Segunda primeiro (extract_api.py)!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    normalize_users()