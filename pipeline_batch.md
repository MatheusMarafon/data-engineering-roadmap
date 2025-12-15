flowchart LR
    A[Arquivo CSV] --> B[Extração - Python]
    B --> C[Transformação - Pandas]
    C --> D[Banco de Dados - PostgreSQL]
    D --> E[Consumo - SQL / Relatórios]
