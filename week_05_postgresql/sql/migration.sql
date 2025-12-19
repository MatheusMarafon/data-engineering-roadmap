drop table if exists pedidos_analise;
drop table if exists clientes_analise;
drop table if exists relatorio_analise;

create table clientes_analise (
	id serial primary key,
	nome varchar(50),
	estado char(2)	
);

create table pedidos_analise (
	id serial primary key,
	cliente_id int,
	valor decimal(10,2)
);

insert into clientes_analise (nome, estado) values
('Ana', 'SP'), ('Bruno','RJ'), ('Carlos','MG'), ('Diana','SP');

insert into pedidos_analise (cliente_id, valor) values
(1, 100.00), (1, 200.00),
(2, 50.00), 
(3, 300.00), (3, 50.00),
(4, 1000.00);


create table relatorio_cache (
	id serial primary key,
	nome_cliente varchar(50),
	estado_cliente char(2),
	total_gasto decimal(10,2)
);

insert into relatorio_cache (nome_cliente, estado_cliente, total_gasto)
select
	c.nome,
	c.estado,
	sum(p.valor)
from clientes_analise c
join pedidos_analise p on c.id = p.cliente_id
group by c.nome, c.estado;


select * from relatorio_cache;