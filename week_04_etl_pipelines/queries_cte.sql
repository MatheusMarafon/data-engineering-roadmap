-- Objetivo: ver os nomes dos clientes que compram itens da categoria 'Eletronicos'

-- Jeito antigo: difícil de ler porque lê de dentro pra fora
select name
from raw.users
where id in (
	select user_id
	from raw.sales
	where product_id in (
		select id 
		from raw.products
		where category = 'Eletronicos'
	)
);

-- Jeito profissional (CTE)
with produtos_eletronicos as (
	-- passo 1: achar quais produtos estão na categoria eletronicos
	select id 
	from raw.products
	where category = 'Eletronicos'
),
vendas_filtradas as(
	-- passo 2: achar as vendas desses produtos
	select user_id
	from raw.sales
	where product_id in (select id from produtos_eletronicos)
)
-- passo 3: pegar o nome do usuário final
select u.name
from raw.users u
where u.id in (select user_id from vendas_filtradas);



-- Bônus: Análise de Gastos (CTE + JOIN)
with vendas_completas as (
	select user_id, total
	from raw.sales
	where status = 'completed'
)
select 
	u.name,
	v.total
from raw.users u
inner join vendas_completas v on u.id = v.user_id


