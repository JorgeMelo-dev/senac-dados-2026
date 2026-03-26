CREATE DATABASE bco_relacional;

USE bco_relacional;

SET GLOBAL local_infile = 1;

CREATE TABLE clientes (
id INT PRIMARY KEY,
nome VARCHAR(100) NOT NULL);

LOAD DATA INFILE 'C:/Users/melo.jorge/Documents/BaseDados/clientes.csv'
INTO TABLE clientes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, nome);

CREATE TABLE pedidos (
id INT PRIMARY KEY,
cliente_id INT,
total DECIMAL(10,2),
FOREIGN KEY (cliente_id) REFERENCES clientes(id));

LOAD DATA INFILE 'C:/Users/melo.jorge/Documents/BaseDados/pedidos.csv'
INTO TABLE pedidos
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, cliente_id, total);
