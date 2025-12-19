-- 1. Limpeza
DROP TABLE IF EXISTS vendas;

-- 2. Criação (Agora com Categoria!)
CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    vendedor VARCHAR(50),
    categoria VARCHAR(50),
    valor DECIMAL(10, 2)
);

-- 3. Inserindo dados variados
INSERT INTO vendas (vendedor, categoria, valor) VALUES
('Ana', 'Eletrônicos', 3500.00),  -- Notebook
('Bruno', 'Eletrônicos', 800.00),  -- Monitor
('Carlos', 'Eletrônicos', 50.00),  -- Mouse
('Ana', 'Móveis', 1200.00),        -- Cadeira
('Bruno', 'Móveis', 500.00),       -- Mesa
('Carlos', 'Móveis', 1200.00),     -- Outra Cadeira (empate proposital)
('Ana', 'Livros', 45.00),
('Carlos', 'Livros', 80.00);



select
	vendedor,
	categoria,
	valor,
	row_number() over (partition by categoria order by valor desc) as ranking
from vendas;