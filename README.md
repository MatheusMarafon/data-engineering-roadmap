# Data Engineering Roadmap

Este repositório documenta minha jornada prática em Engenharia de Dados, focando na construção de pipelines robustos, qualidade de dados, automação e boas práticas de mercado.

O projeto segue um cronograma intensivo de 12 semanas, cobrindo desde os fundamentos até a implementação de orquestradores em nuvem.

## Objetivos
Desenvolver competências técnicas em:
- Linguagens: Python (Pandas, Numpy, APIs) e SQL Avançado.
- Banco de Dados: PostgreSQL e Modelagem Dimensional.
- Engenharia: ETL/ELT, Idempotência, Logging e Tratamento de Erros.
- Orquestração: Airflow e Cron.
- Cloud: AWS (S3, RDS, IAM).

## Estrutura e Progresso
Cada pasta representa uma etapa do cronograma de estudos.

| Pasta | Tópico Principal | Status |
| :--- | :--- | :---: |
| week_01_fundamentos | Conceitos de ED e Ambientação | [x] |
| week_02_python_dados_1 | Pandas, Numpy e Leitura de Arquivos | [x] |
| week_03_python_dados_2 | APIs, Requests e Robustez | [x] |
| week_04_sql_profissional_1 | Joins, CTEs e Consultas Complexas | [x] |
| week_05_sql_profissional_2 | Window Functions e Performance | [x] |
| week_06_etl_pratica | Pipeline ETL Completo (Python + Postgres) | [x] |
| week_07_postgres_modelagem | Modelagem de Dados e DDL | [x] |
| week_08_automacao_cron | Scripts Automatizados | [x] |
| week_09_airflow_concepts | DAGs e Operadores | [x] |
| week_10_aws_free_tier | Integração com Cloud (S3/RDS) | [x] |
| week_11_airflow_aws | Pipeline Híbrido | [x] |
| week_12_portfolio_final | Projeto Final de Encerramento | [x] |

## Como Executar (Exemplo da Semana 6)
Para rodar o pipeline ETL desenvolvido na Semana 6:

1. Instale as dependências:
pip install -r requirements.txt

2. Certifique-se de ter um banco PostgreSQL em execução.

3. Execute o pipeline via terminal:
cd week_06_etl_pratica/python
python main.py --arquivo ../data/vendas_internacionais.csv


## Painel de Observabilidade (Pipeline Automatizado)

Este painel registra as últimas execuções e métricas do pipeline de ETL (`week_08`).

| Data de Referência | Data da Execução | Status | Linhas Processadas | Tipo |
| :--- | :--- | :--- | :---: | :--- |
| **2026-01-05** | 2026-01-05 14:35 | Sucesso | 3 | Agendado (Cron) |
| **2024-01-01** | 2026-01-05 15:10 | Sucesso | 3 | Backfill |
| **2024-01-02** | 2026-01-05 15:10 | Sucesso | 3 | Backfill |
| **2024-01-03** | 2026-01-05 15:10 | Sucesso | 3 | Backfill |
| **2024-01-04** | 2026-01-05 15:10 | Sucesso | 3 | Backfill |
| **2024-01-05** | 2026-01-05 15:10 | Sucesso | 3 | Backfill |
---
Desenvolvido como parte do meu portfólio de Engenharia de Dados.
