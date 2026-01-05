CREATE TABLE IF NOT EXISTS dim_produtos AS
SELECT
    id_produtos AS sk_produto,
    nome AS nm_produto,
    criado_em AS dt_carga
FROM produtos;

ALTER TABLE dim_produtos ADD PRIMARY KEY (sk_produto);


CREATE TABLE IF NOT EXISTS dim_tempo AS
SELECT DISTINCT
    CAST(TO_CHAR(data_venda, 'YYYYMMDD') AS INTEGER) AS sk_tempo,
    CAST(data_venda AS DATE) AS ft_completa,
    CAST(TO_CHAR(data_venda, 'YYYY') AS INTEGER) AS nr_ano,
    CAST(TO_CHAR(data_venda, 'MM') AS INTEGER) AS nr_mes,
    TO_CHAR(data_venda, 'Month') AS nm_mes,
    TO_CHAR(data_venda, 'Q') AS nr_trimestre,
    TO_CHAR(data_venda, 'Day') AS nm_dia_semana
FROM vendas_consolidadas
WHERE data_venda IS NOT NULL;

ALTER TABLE dim_tempo ADD PRIMARY KEY (sk_tempo);

CREATE TABLE IF NOT EXISTS fato_vendas AS
SELECT
    v.id_venda_original AS id_transacao,
    p.sk_produto,
    CAST(TO_CHAR(v.data_venda, 'YYYYMMDD') AS INTEGER) AS sk_tempo,

    v.valor_original,
    v.moeda_origem,
    v.cotacao_dia AS valor_cotacao,
    v.valor_em_brl AS valor_total_brl

FROM vendas_consolidadas v
LEFT JOIN dim_produtos p ON v.id_produto_fk = p.sk_produto;

CREATE INDEX IF NOT EXISTS idx_fato_produto ON fato_vendas(sk_produto);
CREATE INDEX IF NOT EXISTS idx_fato_tempo ON fato_vendas(sk_tempo);

SELECT 'Star Schema criado com sucesso!' AS status;