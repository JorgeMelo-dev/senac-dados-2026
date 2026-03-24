CREATE DATABASE bancosenac;

USE bancosenac;

CREATE TABLE vendas (
data DATE,
produto VARCHAR(100),
categoria VARCHAR(100),
valor_unitario DECIMAL(10,2),
quantidade INT,
cliente VARCHAR(100),
cidade VARCHAR(100),
estado VARCHAR(2)
);

SET GLOBAL local_infile = 1;

LOAD DATA INFILE 'C:/Users/melo.jorge/Documents/BaseDados/vendas.csv'
INTO TABLE vendas
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(data, produto, categoria, valor_unitario,
quantidade, cliente, cidade, estado);

select * from vendas;

SELECT produto, valor_unitario from vendas;

select max(valor_unitario) from vendas;

select data, produto, categoria, valor_unitario, cidade 
from vendas 
where cidade = "Rio de Janeiro";

select produto, sum(valor_unitario * quantidade) ValorVendido
from vendas
group by produto
order by ValorVendido desc;

select v.produto, v.ValorVendido 
from
(
select produto, sum(valor_unitario * quantidade) ValorVendido
from vendas
group by produto
) v
where v.ValorVendido > 3000.00
order by v.ValorVendido desc;
