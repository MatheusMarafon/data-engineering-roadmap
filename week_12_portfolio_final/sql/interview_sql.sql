-- CONFIGURAÇÃO DO AMBIENTE 

-- Tabela de Funcionarios 
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    salary DECIMAL(10,2),
    manager_id INT, -- Para testar Self Joins e Recursão
    hire_date DATE
);

-- Tabela de Vendas 
CREATE TABLE sales (
    sale_id SERIAL PRIMARY KEY,
    emp_id INT,
    sale_date DATE,
    amount DECIMAL(10,2)
);

-- Inserindo Dados Fictícios
INSERT INTO employees (name, dept_id, salary, manager_id, hire_date) VALUES
('Carlos', 1, 10000, NULL, '2020-01-01'), -- CEO
('Ana', 1, 8000, 1, '2021-06-15'),        -- Reporta ao Carlos
('Bruno', 2, 7000, 1, '2021-03-10'),      -- Reporta ao Carlos
('Daniela', 2, 6000, 3, '2022-01-05'),    -- Reporta ao Bruno
('Eduardo', 2, 6500, 3, '2022-02-20'),    -- Reporta ao Bruno
('Fernanda', 3, 5000, 2, '2023-05-01');   -- Reporta à Ana

INSERT INTO sales (emp_id, sale_date, amount) VALUES
(3, '2024-01-01', 500), (3, '2024-01-02', 1500), (3, '2024-01-03', 200),
(4, '2024-01-01', 300), (4, '2024-01-02', 400),
(5, '2024-01-05', 2000), (5, '2024-01-06', 100);


-- 1: JOINS & AGREGAÇÕES 
SELECT 
    e.name AS funcionario,
    e.salary AS salario_func,
    m.name AS gerente,
    m.salary AS salario_gerente
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;


-- 2. Liste todos os funcionários e o total de vendas deles. Se não vendeu nada, mostre 0.
SELECT 
    e.name,
    COALESCE(SUM(s.amount), 0) AS total_vendas
FROM employees e
LEFT JOIN sales s ON e.emp_id = s.emp_id
GROUP BY e.name;


-- 2: WINDOW FUNCTIONS 
-- 3. Rankeie os funcionários por salário dentro de cada departamento (do maior para o menor).
SELECT 
    name,
    dept_id,
    salary,
    RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank_salario
FROM employees;


-- 4. Calcule a "Média Móvel" de vendas dos últimos 3 dias para cada vendedor.
SELECT 
    emp_id,
    sale_date,
    amount,
    AVG(amount) OVER (
        PARTITION BY emp_id 
        ORDER BY sale_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS media_movel_3dias
FROM sales;


-- 5. Qual a diferença de venda de um dia para o dia anterior (Delta)?
SELECT 
    emp_id,
    sale_date,
    amount AS venda_atual,
    LAG(amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS venda_anterior,
    amount - LAG(amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS diferenca
FROM sales;


-- 6. Total Acumulado (Running Total) de vendas por funcionário ao longo do tempo.

SELECT 
    emp_id,
    sale_date,
    amount,
    SUM(amount) OVER (PARTITION BY emp_id ORDER BY sale_date) AS total_acumulado
FROM sales;


-- 3: CTES & CONSULTAS COMPLEXAS (Nível Sênior)

-- 7. Encontre o "Top 1" vendedor de cada departamento (quem mais vendeu no total).
WITH VendasPorFuncionario AS (
    SELECT 
        e.emp_id,
        e.name,
        e.dept_id,
        COALESCE(SUM(s.amount), 0) AS total_vendido
    FROM employees e
    LEFT JOIN sales s ON e.emp_id = s.emp_id
    GROUP BY e.emp_id, e.name, e.dept_id
),
RankVendas AS (
    SELECT 
        *,
        RANK() OVER (PARTITION BY dept_id ORDER BY total_vendido DESC) as rank
    FROM VendasPorFuncionario
)
SELECT name, dept_id, total_vendido
FROM RankVendas
WHERE rank = 1;


-- 8. Identifique funcionários "fantasmas" (que não venderam nada nos últimos 3 meses).
SELECT name
FROM employees e
WHERE NOT EXISTS (
    SELECT 1 
    FROM sales s 
    WHERE s.emp_id = e.emp_id 
    AND s.sale_date > CURRENT_DATE - INTERVAL '3 months'
);


-- 9. (Avançado) Hierarquia Recursiva: Liste todos os subordinados diretos e indiretos do "Carlos" (ID 1).
WITH RECURSIVE Subordinados AS (
    -- Caso Base: Quem reporta direto pro Carlos
    SELECT emp_id, name, manager_id, 1 as nivel
    FROM employees
    WHERE manager_id = 1
    
    UNION ALL
    
    -- Parte Recursiva: Quem reporta pra quem já achamos
    SELECT e.emp_id, e.name, e.manager_id, s.nivel + 1
    FROM employees e
    INNER JOIN Subordinados s ON e.manager_id = s.emp_id
)
SELECT * FROM Subordinados;


-- 10. Pivot de Dados: Transforme as vendas (linhas) em colunas (Jan, Fev, Mar).
SELECT 
    emp_id,
    SUM(amount) FILTER (WHERE EXTRACT(MONTH FROM sale_date) = 1) AS vendas_jan,
    SUM(amount) FILTER (WHERE EXTRACT(MONTH FROM sale_date) = 2) AS vendas_fev,
    SUM(amount) FILTER (WHERE EXTRACT(MONTH FROM sale_date) = 3) AS vendas_mar
FROM sales
GROUP BY emp_id;

