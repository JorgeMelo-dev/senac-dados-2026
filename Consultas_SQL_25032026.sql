USE bco_relacional;

SELECT *
FROM clientes;

SELECT *
FROM pedidos;

SELECT clientes.nome, pedidos.id, pedidos.total
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;

SELECT clientes.nome, pedidos.id, pedidos.total
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;
