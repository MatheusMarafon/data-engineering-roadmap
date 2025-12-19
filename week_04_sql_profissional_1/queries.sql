-- 1. INNER JOIN (A Interseção)
SELECT 
    u.name AS cliente, 
    s.total, 
    s.status
FROM raw.users u
INNER JOIN raw.sales s ON u.id = s.user_id;

-- 2. LEFT JOIN (A Esquerda prevalece)
SELECT 
    u.name AS cliente,
    s.id AS id_venda,
    s.total
FROM raw.users u
LEFT JOIN raw.sales s ON u.id = s.user_id;

-- 3. JOIN TRIPLO (O Poderoso)
SELECT 
    u.name AS cliente,
    p.name AS produto_comprado,
    p.price AS preco_unitario,
    s.quantity AS quantidade,
    s.total AS total_pago
FROM raw.sales s
INNER JOIN raw.users u ON s.user_id = u.id      -- Liga Venda com Usuário
INNER JOIN raw.products p ON s.product_id = p.id; -- Liga Venda com Produto

-- 4. CROSS JOIN (O Perigoso)

SELECT 
    u.name AS cliente,
    p.name AS produto
FROM raw.users u
CROSS JOIN raw.products p;