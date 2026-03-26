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
