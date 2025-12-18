-- == 1. FAXINA GERAL (Apaga tudo para não dar erro de "já existe") ==
DROP SCHEMA IF EXISTS raw CASCADE;
DROP SCHEMA IF EXISTS processed CASCADE;
DROP SCHEMA IF EXISTS gold CASCADE;

-- == 2. CRIAÇÃO DAS PASTAS (Agora elas vão existir de certeza) ==
CREATE SCHEMA raw;
CREATE SCHEMA processed;
CREATE SCHEMA gold;

-- == 3. CRIAÇÃO DAS TABELAS (Dentro da pasta 'raw') ==

-- Tabela Clientes
CREATE TABLE raw.users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(20) DEFAULT 'customer',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela Produtos
CREATE TABLE raw.products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE
);

-- Tabela Vendas
CREATE TABLE raw.sales (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES raw.users(id),
    product_id INT REFERENCES raw.products(id),
    quantity INT DEFAULT 1,
    total DECIMAL(10, 2),
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20)
);