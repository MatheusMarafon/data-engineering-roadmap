import pandas as pd
from sqlalchemy import create_engine, text

DB_CONFIG = "postgresql+psycopg2://postgres:admin@localhost:5432/postgres"


def run_data_quality_checks():
    print("Iniciando Verificação de Qualidade de Dados...")

    try:
        engine = create_engine(DB_CONFIG)

        # Carrega dados da Fato para analise
        query = """
        SELECT 
            id_transacao, 
            valor_original, 
            valor_total_brl, 
            sk_tempo,
            moeda_origem 
        FROM fato_vendas
        """
        df = pd.read_sql(query, engine)
        print(f"Dados esperados: {len(df)} linhas.")

        report = []

        # 1ª checagem: números nulos
        # ID e Valor BRL não podem ser nulos
        nulos_id = df["id_transacao"].isnull().sum()
        nulos_valor = df["valor_total_brl"].isnull().sum()

        if nulos_id > 0 or nulos_valor > 0:
            report.append(
                f"[CRÍTICO] Encontrados valores nulos! (IDs: {nulos_id}, Valores: {nulos_valor})"
            )
        else:
            report.append("[OK] Completudo: Sem valores nulos críticos.")

        # 2ª checagem: consistencia de valores
        # não existe venda negativa ou zerada
        vendas_invalidas = df[df["valor_total_brl"] <= 0]

        if len(vendas_invalidas) > 0:
            report.append(
                f"[CRÍTICO] {len(vendas_invalidas)} vendas com valor menor ou igual a zero!"
            )
        else:
            report.append("[OK] Consistencia: Todos os valores de venda sao positivos.")

        # 3ª checagem: validade de dominio
        # moedas aceitas sao apenas USD, EUR, BRL, GPB, etc.
        moedas_validas = ["USD", "EUR", "BRL", "GPB"]
        moedas_estranhas = df[~df["moeda_origem"].isin(moedas_validas)][
            "moeda_origem"
        ].unique()

        if len(moedas_estranhas) > 0:
            report.append(
                f"[AVISO] Moedas desconecidas encontradas: {moedas_estranhas}"
            )
        else:
            report.append(["[OK] Dominio: Todas as moedas sao validas."])

        # resultados
        print("\n" + "=" * 40)
        print("Relatório de Qualidade")
        print("=" * 40)
        for linha in report:
            print(linha)
        print("-" * 40)

    except Exception as e:
        print(f"[ERRO] Falha na conexão ou execução: {e}")


if __name__ == "__main__":
    run_data_quality_checks()
