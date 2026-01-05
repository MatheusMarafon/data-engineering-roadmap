-- 1. Criar tabela (Sem vírgula no final)
CREATE TABLE IF NOT EXISTS produtos (
    id_produtos SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL UNIQUE,
    criado_em TIMESTAMP DEFAULT NOW() 
);

-- 2. Inserir dados (INSERT INTO em vez de SELECT INTO)
INSERT INTO produtos(nome)
SELECT DISTINCT produto  
FROM vendas_consolidadas
WHERE produto IS NOT NULL 
ON CONFLICT (nome) DO NOTHING;

-- 3. Criar coluna FK
ALTER TABLE vendas_consolidadas
ADD COLUMN IF NOT EXISTS id_produto_fk INT;

-- 4. Atualizar IDs (UPDATE sem a palavra TABLE)
UPDATE vendas_consolidadas v
SET id_produto_fk = p.id_produtos
FROM produtos p
WHERE v.produto = p.nome;

-- 5. Criar restrição (Constraint)
ALTER TABLE vendas_consolidadas
ADD CONSTRAINT fk_vendas_produtos
FOREIGN KEY (id_produto_fk) REFERENCES produtos(id_produtos);

-- 6. Índice
CREATE INDEX IF NOT EXISTS idx_vendas_id_produto
ON vendas_consolidadas(id_produto_fk);