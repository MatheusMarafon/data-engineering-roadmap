#  Arquitetura e Conceitos de Engenharia de Dados

Este documento reúne os principais conceitos teóricos, padrões de arquitetura e trade-offs exigidos em entrevistas para Engenharia de Dados.

---

##  Diagramas de Arquitetura

### 1. Arquitetura Medalhão (Bronze / Silver / Gold)

**Bronze (Raw):**  
Dados brutos, exatamente como vieram da fonte. Ninguém mexe aqui.

**Silver (Refined):**  
Dados limpos, deduplicados e tipados. Prontos para Data Science.

**Gold (Curated):**  
Dados agregados, regras de negócio aplicadas (KPIs). Prontos para BI.

---

### 2. ETL vs ELT

A evolução do processamento de dados com a nuvem.

**ETL (Extract-Transform-Load):**  
Transforma antes de salvar. Bom para segurança e quando o armazenamento é caro.

**ELT (Extract-Load-Transform):**  
Carrega tudo bruto rápido, transforma depois.  
Padrão moderno (BigQuery, Redshift, Snowflake), pois armazenamento é barato e processamento é escalável.

---

##  Perguntas e Respostas (Q&A)

###  Fundamentos

<details>
<summary><strong>1. Qual a diferença entre Data Lake e Data Warehouse?</strong></summary>

**Data Lake:**  
Armazena dados estruturados e não estruturados (imagens, logs, CSVs).  
Schema-on-Read (define o esquema na hora de ler).  
Ex: S3, Azure Blob.  
Mais barato.

**Data Warehouse:**  
Armazena apenas dados estruturados e relacionais.  
Schema-on-Write (precisa definir tabela antes).  
Otimizado para SQL rápido.  
Ex: Redshift, BigQuery, Snowflake.

</details>

<details>
<summary><strong>2. O que é OLTP vs OLAP?</strong></summary>

**OLTP (Online Transaction Processing):**  
Bancos operacionais (Postgres do app).  
Foco em transações rápidas (INSERT, UPDATE) e consistência.

**OLAP (Online Analytical Processing):**  
Bancos analíticos (DW).  
Foco em leitura pesada e agregações (SUM, AVG) de milhões de linhas.  
Arquitetura colunar.

</details>

<details>
<summary><strong>3. O que é o Teorema CAP?</strong></summary>

Em um sistema distribuído, você só pode garantir **2 de 3**:

- **Consistency:** Todos veem o mesmo dado ao mesmo tempo.  
- **Availability:** O sistema responde sempre.  
- **Partition Tolerance:** O sistema continua funcionando mesmo com falha de rede.

Bancos SQL tradicionais focam em **CA**.  
Bancos NoSQL geralmente focam em **AP**.

</details>

---

##  Orquestração (Airflow)

<details>
<summary><strong>4. O que é Idempotência? Por que é vital no Airflow?</strong></summary>

Idempotência significa que rodar o mesmo pipeline várias vezes gera sempre o mesmo resultado.

**Ruim:**  
Executar inserts sem controle — se rodar duas vezes, duplica dados.

**Bom:**  
Executar deletes/merges antes de inserir — pode rodar N vezes sem duplicar.

Vital porque o Airflow possui **retries automáticos**.

</details>

<details>
<summary><strong>5. O que é Backfill?</strong></summary>

Processar dados do passado.

**Exemplo:**  
A DAG foi criada hoje, mas você quer processar dados desde Janeiro.

No Airflow:
- `start_date` no passado  
- `catchup=True`

Isso faz o Airflow executar todas as execuções pendentes.

</details>

---

##  Modelagem de Dados

<details>
<summary><strong>6. Star Schema vs Snowflake Schema?</strong></summary>

**Star Schema:**  
Tabela Fato central + Dimensões desnormalizadas.  
Menos JOINs → consultas mais rápidas.  
Padrão Kimball.

**Snowflake Schema:**  
Dimensões normalizadas em várias tabelas.  
Economiza espaço, mas aumenta custo de JOINs.

</details>

<details>
<summary><strong>7. O que são SCDs (Slowly Changing Dimensions)?</strong></summary>

Como lidar com mudanças de dados dimensionais (ex: cliente mudou endereço).

- **Tipo 0:** Nunca muda.  
- **Tipo 1:** Sobrescreve (perde histórico).  
- **Tipo 2:** Cria nova linha com data de início/fim e flag de ativo.  
   Mais usado em Engenharia de Dados.

</details>

---

##  Big Data & Arquivos

<details>
<summary><strong>8. Por que usar Parquet em vez de CSV?</strong></summary>

- Colunar → lê apenas as colunas necessárias  
- Alta compressão (Snappy, Gzip)  
- Schema embutido → menos erro de tipagem  
- Muito mais rápido e barato em engines como Spark e Athena

</details>

<details>
<summary><strong>9. O que é Particionamento?</strong></summary>

Organizar dados em pastas lógicas, por exemplo:

ano=2024/mes=01/dia=15/

Permite **Partition Pruning**, onde o engine lê apenas os dados necessários, reduzindo custo e tempo de execução.

</details>

---

**Estudos realizados por Matheus Marafon**
