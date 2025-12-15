# Semana 1 — Fundamentos de Engenharia de Dados

Objetivo da semana:
- Compreender o papel do engenheiro de dados
- Entender arquiteturas de dados
- Diferenciar batch e streaming
- Introdução à qualidade e governança de dados

## Batch vs Streaming

| Critério        | Batch Processing                         | Streaming Processing                      |
|-----------------|------------------------------------------|-------------------------------------------|
| Latência        | Alta (minutos / horas)                   | Baixa (segundos / tempo real)             |
| Volume          | Grandes volumes históricos               | Fluxo contínuo de eventos                 |
| Complexidade    | Menor                                    | Maior                                     |
| Custo           | Mais barato                              | Mais caro                                 |
| Infraestrutura  | Simples                                  | Mais complexa                             |
| Casos de uso    | Relatórios, BI, faturamento, ETL diário  | Fraude, monitoramento, eventos em tempo real |
| Exemplo         | CSV diário para data warehouse           | Eventos de clique, sensores, logs         |
