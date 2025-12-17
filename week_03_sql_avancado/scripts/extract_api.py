import requests
import json
import os


def extract_users():
    url = "https://jsonplaceholder.typicode.com/users"

    caminho_pasta = r"C:\Users\matheus.r\Desktop\data-engineering-roadmap\week_03_sql_avancado\data\raw"
    nome_arquivo = "users.json"

    caminho_saida = os.path.join(caminho_pasta, nome_arquivo)
    print(f"Conectando a url: {url}")

    try:
        # Faz a requisição (GET)
        # Usamos timeout = 10 (10 seg) para caso o servidor demore
        response = requests.get(url, timeout=10)

        # Verificando o STATUS
        # 200 = Sucesso
        # 404 = Não encontrado
        # 500 = Erro no servidor
        if response.status_code == 200:
            data = response.json()
            print(f"Sucesso! {len(data)} usuários baixados."),

            os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

            with open(caminho_saida, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=5, ensure_ascii=False)

            print(f"Arquivo salvo em: {caminho_saida}")
        else:
            print(f"Erro na requisição: {response.status_code}")
    except requests.exceptions.Timeout:
        print(
            "Erro: O servidor demorou muito para responder (Timeout)."
        )  # Neste caso, uma opção é aumentar o timeout
    except requests.exceptions.ConnectionError:
        print("Erro: Falha de conexão. Verifique sua internet.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    extract_users()
