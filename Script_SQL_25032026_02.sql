USE bco_relacional;

SET GLOBAL local_infile = 1;

CREATE TABLE usuarios (
usuario_id INT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
pais VARCHAR(40) NOT NULL,
plano VARCHAR(40) NOT NULL,
data_cadastro DATE NOT NULL);

LOAD DATA INFILE 'C:/Users/melo.jorge/Documents/BaseDados/usuarios.csv'
INTO TABLE usuarios
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(usuario_id, nome, email, pais, plano, data_cadastro);


filme_id,titulo,genero,ano_lancamento,duracao_min,classificacao,nota_imdb

CREATE TABLE filmes (
filme_id INT PRIMARY KEY,
titulo VARCHAR(100) NOT NULL,
genero VARCHAR(50) NOT NULL,
ano_lancamento INT,

cliente_id INT,
total DECIMAL(10,2),
FOREIGN KEY (cliente_id) REFERENCES clientes(id));

LOAD DATA INFILE 'C:/Users/melo.jorge/Documents/BaseDados/pedidos.csv'
INTO TABLE pedidos
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, cliente_id, total);
