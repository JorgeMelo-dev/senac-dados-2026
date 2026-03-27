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


CREATE TABLE filmes (
filme_id INT PRIMARY KEY,
titulo VARCHAR(100) NOT NULL,
genero VARCHAR(50) NOT NULL,
ano_lancamento INT NOT NULL,
duracao_min INT NOT NULL,
classificacao VARCHAR(2) NOT NULL,
nota_imdb DECIMAL(5,2));

LOAD DATA INFILE 'C:/Users/melo.jorge/Documents/BaseDados/filmes.csv'
INTO TABLE filmes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(filme_id, titulo, genero, ano_lancamento, duracao_min, classificacao, nota_imdb);


CREATE TABLE avaliacoes (
avaliacao_id INT PRIMARY KEY,
usuario_id INT NOT NULL,
filme_id INT NOT NULL,
nota DECIMAL(5,2) NOT NULL,
data_avaliacao DATE NOT NULL,
assistiu_completo VARCHAR(1) NOT NULL,
FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id),
FOREIGN KEY (filme_id) REFERENCES filmes(filme_id));

LOAD DATA INFILE 'C:/Users/melo.jorge/Documents/BaseDados/avaliacoes.csv'
INTO TABLE avaliacoes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(avaliacao_id, usuario_id, filme_id, nota, data_avaliacao, assistiu_completo);
