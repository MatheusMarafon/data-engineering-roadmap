-- 1. Limpeza
DROP TABLE IF EXISTS faturamento;

-- 2. Criação
CREATE TABLE faturamento (
    data_fechamento DATE,
    total DECIMAL(10,2)
);

-- 3. Inserindo dados (Simulando 5 semanas)
INSERT INTO faturamento (data_fechamento, total) VALUES
('2023-01-01', 10000.00), -- Semana 1
('2023-01-08', 12000.00), -- Semana 2 (Cresceu)
('2023-01-15', 11000.00), -- Semana 3 (Caiu)
('2023-01-22', 15000.00), -- Semana 4 (Cresceu muito)
('2023-01-29', 15000.00); -- Semana 5 (Estagnou)


select 
	data_fechamento,
	total,
	lag(total) over (order by data_fechamento) as semana_anterior
from faturamento;

select
	data_fechamento,
	total,
	lag(total) over (order by data_fechamento) as semana_anterior,
	total - lag(total) over (order by data_fechamento) as diferenca_semanal
from faturamento;


select 
	data_fechamento,
	total,
	lag(total) over (order by data_fechamento) as semana_anterior,
	total - lag(total) over (order by data_fechamento) as diferenca,
	avg(total) over (
		order by data_fechamento
		rows between 1 preceding and current row		
	) as media_movel
from faturamento;
	