import pandas as pd


# Função que processa os dados e transforma
def process_data(df, cotacoes):
    print("Iniciando transformação de dados...")

    try:
        linhas_antes = len(df)
        df = df.drop_duplicates(subset=["id_venda"], keep="last")
        linhas_depois = len(df)

        if linhas_antes > linhas_depois:
            print(f" {linhas_antes - linhas_depois} duplicadas removidas.")

        df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")
        df = df.dropna(subset=["data_venda"])

        cotacoes["BRL"] = 1.0

        df["cotacao_dia"] = df["moeda"].map(cotacoes)

        if df["cotacao_dia"].isnull().any():
            qtd_erros = df["cotacao_dia"].isnull().sum()
            print(f"{qtd_erros} vendas com moedas desconhecidas removidas.")
            df = df.dropna(subset=["cotacao_dia"])

        df["valor_em_brl"] = df["valor_original"] * df["cotacao_dia"]
        df["valor_em_brl"] = df["valor_em_brl"].round(2)

        df_final = df.rename(
            columns={"id_venda": "id_venda_original", "moeda": "moeda_origem"}
        )

        colunas_finais = [
            "id_venda_original",
            "data_venda",
            "produto",
            "valor_original",
            "moeda_origem",
            "cotacao_dia",
            "valor_em_brl",
        ]

        print(f"Transformação concluída! {len(df_final)} registros finalizados.")
        return df_final[colunas_finais]

    except Exception as e:
        print(f"Erro crítico nas transformações: {e}")
        raise


if __name__ == "__main__":
    data = {
        "id_venda": [1, 2, 3, 4],
        "data_venda": ["2023-01-01", "2023-01-02", "2023-01-02", "errada"],
        "produto": ["PC", "Mouse", "Mouse", "Tela"],
        "valor_original": [1000, 50, 50, 200],
        "moeda": ["USD", "EUR", "EUR", "JPY"],
    }
    cotacoes_mock = {"USD": 5.0, "EUR": 6.0}
    print("TESTANDO...")
    df_limpo = process_data(pd.DataFrame(data), cotacoes_mock)
    print(df_limpo)
