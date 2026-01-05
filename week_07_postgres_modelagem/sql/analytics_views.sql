-- Consertando erro de digitação da tarefa de terça
ALTER TABLE dim_tempo 
RENAME COLUMN ft_completa TO dt_completa;

-- Tarefa quarta
CREATE OR REPLACE VIEW vw_vendas_kpi AS
SELECT 
    f.id_transacao,
    t.dt_completa AS data_venda,
    p.nm_produto AS produto,
    f.valor_total_brl AS valor_venda,
    f.moeda_origem,
    t.nm_mes,
    t.nr_ano
FROM fato_vendas f
JOIN dim_produtos p ON f.sk_produto = p.sk_produto
JOIN dim_tempo t ON f.sk_tempo = t.sk_tempo;


CREATE MATERIALIZED VIEW IF NOT EXISTS mv_vendas_diarias AS
SELECT 
    t.dt_completa,
    t.nr_ano,
    t.nm_mes,
    COUNT(f.id_transacao) AS qtd_vendas,
    SUM(f.valor_total_brl) AS faturamento_total,
    AVG(f.valor_total_brl) AS ticket_medio
FROM fato_vendas f
JOIN dim_tempo t ON f.sk_tempo = t.sk_tempo
GROUP BY t.dt_completa, t.nr_ano, t.nm_mes
ORDER BY t.dt_completa DESC
WITH NO DATA; 
REFRESH MATERIALIZED VIEW mv_vendas_diarias;

CREATE INDEX IF NOT EXISTS idx_mv_vendas_data ON mv_vendas_diarias(dt_completa);

SELECT 'Relatório Diário pronto!' as status;


