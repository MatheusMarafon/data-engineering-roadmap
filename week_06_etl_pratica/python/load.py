import pandas as pd
from sqlalchemy import create_engine, text
import os

# Configuração do DB (sem 'db_pass' porque o banco não tem senha)
db_user = "postgres"
db_host = "localhost"
db_port = "5432"
db_name = "postgres"
database_url = f"postgresql://{db_user}@{db_host}:{db_port}/{db_name}"

engine = create_engine(database_url)


def carregar_dados(df):
    print("Iniciando carga no DB (upset)...")

    # Condição para verificar se o DF está vazio, se estiver, não há nada para upar
    if df.empty:
        print("DataFrame está vazio. Nada para carregar.")
        return

    try:
        # Criamos uma tabela temporária e jogamos os dados la dentro
        df.to_sql("temp_vendas", engine, if_exists="replace", index=False)

        sql_upsert = text(
            """
            INSERT INTO vendas_consolidadas (
                id_venda_original, data_venda, produto, 
                valor_original, moeda_origem, cotacao_dia, valor_em_brl, data_carga
            )
            SELECT 
                id_venda_original, 
                CAST(data_venda AS DATE), 
                produto, 
                valor_original, 
                moeda_origem, 
                cotacao_dia, 
                valor_em_brl,
                NOW()
            FROM temp_vendas
            ON CONFLICT (id_venda_original) 
            DO UPDATE SET
                valor_em_brl = EXCLUDED.valor_em_brl,
                cotacao_dia = EXCLUDED.cotacao_dia,
                data_carga = NOW();
        """
        )

        with engine.begin() as conn:
            conn.execute(sql_upsert)
            # Limpa o que foi criado (lixo)
            conn.execute(text("DROP TABLE temp_vendas"))
        print(f"Carga consluída! {len(df)} linhas processadas.")

    except Exception as e:
        print(f"Erro ao carregar: {e}")
        raise


if __name__ == "__main__":
    data = {
        "id_venda_original": [101, 102],
        "data_venda": ["2023-10-25", "2023-10-25"],
        "produto": ["Teste A", "Teste B"],
        "valor_original": [100, 200],
        "moeda_origem": ["USD", "USD"],
        "cotacao_dia": [5.0, 5.0],
        "valor_em_brl": [500.0, 1000.0],
    }
    df_teste = pd.DataFrame(data)
    carregar_dados(df_teste)
