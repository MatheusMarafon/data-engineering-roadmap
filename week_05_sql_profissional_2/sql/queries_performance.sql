-- Caso já exista a tabela 'pedidos_log', exclui
drop table if exists pedidos_log;

-- Cria a tabela 'pedidos_log'
create table pedidos_log (
	id serial primary key,
	cod_rastreio int,
	data_registro timestamp default now()
);

-- Inserindo 1 milhão de linhas aleatóriamente
-- 'generate_series' cria os números, 'random()' gera códigos aleatórios
insert into pedidos_log (cod_rastreio)
select (random() * 100000):: int
from generate_series(1, 1000000);

-- Busca sem índice 
explain analyze
select * from pedidos_log where cod_rastreio = 42;


-- Criando o índice na coluna que estamos pesquisando
create index idx_cod_rastreio on pedidos_log(cod_rastreio);


-- Busca com índice 
explain analyze
select * from pedidos_log where cod_rastreio = 42;

-- Relatório de performance
-- Teste realizado com 1 milhão de linhas
-- Teste SEM índice: 56 ms
-- Teste COM índice: 9.5 ms
-- Conclusão: O uso de índice reduziu em  aprox. 83% do tempo