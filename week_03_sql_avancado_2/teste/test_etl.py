import os
import pandas as pd
import pytest

#Caminhos
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_path = os.path.join(base_dir, "data", "raw", "users.json")
processed_path = os.path.join(base_dir, "data", "processed", "api_clean.parquet")

def test_verificar_se_arquivo_raw_existe():
    """verifica se o script de extração (segunda/quinta) funcionou"""
    assert os.path.exists(raw_path), f"ERRO: o arquivo {raw_path} não foi encontrado. Rode o extract_api.py primeiro."

def test_verificar_se_arquivo_processed_exist():
    """verifica se o script de normalização (quarta) funcionou"""
    assert os.path.exists(processed_path), f"ERRO: o arquivo {processed_path} não foi encontrado. Rode o normalize_data.py primeiro."

def test_verificar_colunas_normalizadas():
    """verifica se o JSON foi realmente 'achatado' no parquet"""
    #Primeiro confere se passou no segundo teste
    if os.path.exists(processed_path):
        df = pd.read_parquet(processed_path)
        
        #Confere se possui dados
        assert len(df) > 0, "O arquivo parquet está vazio!"
        colunas_esperadas = ['id', 'name', 'email', 'address.city', 'company.name']

        for coluna in colunas_esperadas:
            assert coluna in df.columns, f"A coluna '{coluna}' está faltando no arquivo final!"