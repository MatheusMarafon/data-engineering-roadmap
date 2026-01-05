import pandas as pd
import requests
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import sys

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s = %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


# Configuração de Retries
def requests_retry_session(
    retries=3,
    backoff_factor=1,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


# Função que extrai CSV
def ler_dados_vendas(caminho_ficheiro):
    logger.info(f"Iniciando leitura do ficheiro: {caminho_ficheiro}")
    try:
        df = pd.read_csv(caminho_ficheiro)
        logger.info(f"Sucesso! {len(df)} linhas carregadas.")
        return df
    except FileNotFoundError:
        logger.error(f"Ficheiro não encontrado: {caminho_ficheiro}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Erro inesperado ao ler CSV: {e}")
        sys.exit(1)


# Função que extrai a API (com Retry)
def buscar_cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL"
    logger.info(f"Conectando com a API de cotações: {url}")

    try:
        response = requests_retry_session().get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        cotacoes = {
            "USD": float(data["USDBRL"]["bid"]),
            "EUR": float(data["EURBRL"]["bid"]),
            "GPB": float(data["GBPBRL"]["bid"]),
        }
        logger.info(f"Cotações obtidas: {cotacoes}")
        return cotacoes

    except Exception as e:
        logger.critical(f"Falha crítica na API após tentativas: {e}")
        sys.exit(1)


if __name__ == "__main__":
    df = ler_dados_vendas("")

    buscar_cotacoes()
