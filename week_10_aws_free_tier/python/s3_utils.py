import boto3
import os
from dotenv import load_dotenv

# Carrega as chaves do arquivo .env
load_dotenv()


# Função que cria conexão com S3
def get_s3_client():
    """Cria conexão com o S3"""
    return boto3.client(
        "s3",
        aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )


# Função que upa um arquivo no S3
def upload_file(file_name, bucket, object_name=None):
    """Sobe um arquivo para o S3"""
    s3_client = get_s3_client()
    try:
        s3_client.upload_file(file_name, bucket, object_name or file_name)
        print(f"Arquivo {file_name} enviado com sucesso!")
    except Exception as e:
        print(f"Erro no upload: {e}")


# Função que baixa um arquivo do S3
def download_file(bucket, object_name, file_name):
    """Baixa um arquivo do S3"""
    s3_client = get_s3_client()
    try:
        s3_client.download_file(bucket, object_name, file_name)
        print(f"Arquivo {file_name} baixado com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar arquivo: {e}")


# Chamada
if __name__ == "__main__":
    # Teste rápido
    with open("teste_aws.txt", "w") as f:
        f.write("Estudo de Engenharia de Dados na AWS!")

    bucket_name = "matheus-datalake-semana10"

    # Salva dentro da pasta raw o txt
    download_file(bucket_name, "raw/teste_aws.txt", "teste_aws.txt")
