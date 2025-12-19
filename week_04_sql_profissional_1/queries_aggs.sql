-- Cria a tabela (Se já existir uma velha, ele apaga antes)
DROP TABLE IF EXISTS vendas;

CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    vendedor VARCHAR(50),
    produto VARCHAR(50),
    valor DECIMAL(10, 2)
);

-- Insere os dados de teste
INSERT INTO vendas (vendedor, produto, valor) VALUES
('Ana', 'Notebook', 3500.00),
('Ana', 'Mouse', 50.00),
('Bruno', 'Teclado', 150.00),
('Bruno', 'Monitor', 800.00),
('Carlos', 'Notebook', 3500.00),
('Ana', 'Cadeira Gamer', 1200.00),
('Bruno', 'Mouse', 50.00);


SELECT 
    vendedor,
    SUM(valor) as total_vendido
FROM vendas
GROUP BY vendedor;


-- Apenas vendedores que bateram a meta de 2000
select
	vendedor,
	sum(valor) as total_vendido
from vendas 
group by vendedor
having sum(valor) > 2000;


-- Quantidade de vendas e ticket medio
select 
	vendedor,
	count (*) as qtd_vendas,
	avg(valor) as ticket_medio
from vendas
group by vendedor;





