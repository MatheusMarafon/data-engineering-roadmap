# Estratégia de Particionamento S3

**Estrutura Escolhida:**
`s3://<bucket_name>/processed/YYYY/MM/DD/<arquivo>`

**Por que usar?**
1. **Partition Pruning (Poda de Partição):** Ao consultar dados de um dia específico (ex: via AWS Athena), a engine ignora fisicamente todos os outros anos e meses, reduzindo drasticamente o I/O e o custo.
2. **Ciclo de Vida (Lifecycle):** Facilita criar regras para arquivar dados antigos (ex: mover a pasta `2024/` inteira para o S3 Glacier após 1 ano).
3. **Organização Lógica:** Permite reprocessamento granular. Se o dia 21 der erro, apago e reprocesso apenas a pasta `21/`.