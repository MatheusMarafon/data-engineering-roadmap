import requests
import json
import os
import time

def extract_posts_paginated():
    url = "https://jsonplaceholder.typicode.com/posts"

    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    diretorio_raiz = os.path.dirname(diretorio_script)
    pasta_destino = os.path.join(diretorio_raiz, "data", "raw")

    os.makedirs(pasta_destino, exist_ok=True)
    print(f"Iniciando extração paginada de: {url}")

    #Pegando da página 1 a 5 (6 representa que vai parar na 6ª página)
    for pagina in range(1, 6):
        try:
            print(f"Baixando página: {pagina}...")

            #Parâmetros da URL
            params = {
                '_page': pagina,
                '_limit': 10 #Limitamos a 10 posts por página
            }

            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()

                nome_arquivo = f"posts_page_{pagina}.json"
                caminho_final = os.path.join(pasta_destino, nome_arquivo)

                with open(caminho_final, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)

                print(f"Salvo: {nome_arquivo}")
            else:
                print(f"Erro na página {pagina}: {response.status_code}")

            time.sleep(1) #Espera de 1 segundo entre as requisições

        except Exception as e:
            print(f"Erro crítico na página {pagina}: {e}")
        print("Processo finalizado!")

if __name__ == "__main__":
    extract_posts_paginated()
