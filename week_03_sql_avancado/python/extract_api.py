import requests
import json
import os
import logging
import time

#Configuração do Logging
logging.basicConfig(
    level=logging.INFO,  #Mostra mensagens de INFO, WARNING e ERROR
    format="%(asctime)s - %(levelname)s - %(message)s",  #Formato: Data - Nível - Msg
    datefmt="%Y-%m-%d %H:%M:%S",
)


def extract_users_with_logging():
    url = "https://jsonplaceholder.typicode.com/users"

    #Caminhos
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    diretorio_raiz = os.path.dirname(diretorio_script)
    pasta_destino = os.path.join(diretorio_raiz, "data", "raw")
    caminho_saida = os.path.join(pasta_destino, "users.json")

    logging.info(f"Iniciando processo de extração para: {url}")

    #Estratégia de Backoff (Tentar de novo)
    max_tentativas = 3

    for tentativa in range(1, max_tentativas + 1):
        try:
            logging.info(f"Tentativa {tentativa} de {max_tentativas}...")

            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                logging.info(f"Download concluído! {len(data)} registros baixados.")
       
                os.makedirs(pasta_destino, exist_ok=True)
                with open(caminho_saida, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)

                logging.info(f"Arquivo salvo com sucesso em: {caminho_saida}")

                break

            else:
                logging.warning(f"A API retornou erro: {response.status_code}")
                #Se não foi sucesso, o loop continua para a próxima tentativa

        except requests.exceptions.Timeout:
            logging.error("Timeout: O servidor demorou para responder.")
        except requests.exceptions.ConnectionError:
            logging.error("Erro de Conexão: Verifique a internet.")
        except Exception as e:
            logging.critical(f"Erro inesperado: {e}")

        #Espera antes de tentar de novo (Backoff)
        if tentativa < max_tentativas:
            tempo_espera = 2 * tentativa  # Espera 2s, depois 4s...
            logging.info(
                f"Aguardando {tempo_espera} segundos para tentar novamente..."
            )
            time.sleep(tempo_espera)
        else:
            logging.error("Todas as tentativas falharam. Abortando.")


if __name__ == "__main__":
    extract_users_with_logging()
