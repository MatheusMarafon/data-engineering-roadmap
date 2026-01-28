# 🌪️ Pipeline de ETL com Apache Airflow e AWS

Este projeto simula um ambiente de Engenharia de Dados moderno, orquestrando dados locais para um Data Lake (S3) e um Data Warehouse (RDS) usando **Docker** e **Airflow**.

![Airflow Logo](https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png)

## 🏗️ Arquitetura
**Fluxo de Dados:**
1. **Extração:** Leitura de arquivos CSV processados localmente.
2. **Data Lake (S3):** Upload particionado (`YYYY/MM/DD`) para custo e performance.
3. **Data Warehouse (RDS):** Carga incremental no PostgreSQL para análise.

## 🛠️ Tecnologias Utilizadas
* **Orquestração:** Apache Airflow 2.x
* **Cloud:** AWS S3 (Bucket), AWS RDS (PostgreSQL)
* **Linguagem:** Python 3.9 (Pandas, Boto3, SQLAlchemy)
* **Infraestrutura:** Docker & Docker Compose

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/MatheusMarafon/data-engineering-roadmap.git](https://github.com/MatheusMarafon/data-engineering-roadmap.git)