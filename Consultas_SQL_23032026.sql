USE bancosenac;

SELECT * FROM vendas 
LIMIT 10;

SELECT produto, valor_unitario from vendas;

SELECT max(valor_unitario) FROM vendas;

SELECT data, produto, categoria, valor_unitario, cidade 
FROM vendas 
WHERE cidade = "Rio de Janeiro";

SELECT produto, sum(valor_unitario * quantidade) AS Valor_Vendido
FROM vendas
GROUP BY produto
ORDER BY Valor_Vendido DESC;

SELECT produto, sum(valor_unitario * quantidade) AS Valor_Vendido
FROM vendas
WHERE categoria = "Eletrônicos"
GROUP BY produto
HAVING Valor_Vendido > 2000.00
ORDER BY Valor_Vendido DESC;

select v.produto, v.ValorVendido 
from
(
select produto, sum(valor_unitario * quantidade) ValorVendido
from vendas
group by produto
) v
where v.ValorVendido > 3000.00
order by v.ValorVendido desc;


-- EXERCÍCIO NÍVEL 1 - 1
SELECT * FROM vendas;

-- EXERCÍCIO NÍVEL 1 - 2
SELECT * 
FROM vendas
WHERE categoria = "Informática";

-- EXERCÍCIO NÍVEL 1 - 3
SELECT * 
FROM vendas
WHERE estado = "RJ";

-- EXERCÍCIO NÍVEL 1 - 4
SELECT * 
FROM vendas
WHERE valor_unitario > 500;

-- EXERCÍCIO NÍVEL 1 - 5
SELECT * 
FROM vendas
WHERE cliente = "Ana Souza";

-- EXERCÍCIO NÍVEL 1 - 6
SELECT * 
FROM vendas
WHERE categoria = "Vestuário"
  AND estado = "PR";

-- EXERCÍCIO NÍVEL 1 - 7
SELECT produto, categoria, valor_unitario 
FROM vendas
WHERE estado = "SP";

-- EXERCÍCIO NÍVEL 2 - 8
SELECT produto, valor_unitario * quantidade AS Valor_Vendido
FROM vendas
ORDER BY Valor_Vendido DESC;

-- EXERCÍCIO NÍVEL 2 - 9
SELECT produto, cliente, quantidade, valor_unitario * quantidade AS Valor_Vendido
FROM vendas
WHERE quantidade > 1
ORDER BY Valor_Vendido DESC;

-- EXERCÍCIO NÍVEL 2 - 10
SELECT *, valor_unitario * quantidade AS Valor_Vendido
FROM vendas
HAVING Valor_Vendido > 1000
ORDER BY Valor_Vendido DESC;

-- EXERCÍCIO NÍVEL 2 - 11
SELECT *, valor_unitario * quantidade AS Valor_Vendido
FROM vendas
WHERE categoria = "Eletrônicos"
ORDER BY Valor_Vendido DESC;

-- EXERCÍCIO NÍVEL 2 - 12
SELECT *, valor_unitario * quantidade AS Valor_Vendido
FROM vendas
HAVING Valor_Vendido > 2000
ORDER BY Valor_Vendido DESC;

-- EXERCÍCIO NÍVEL 3 - 13
SELECT categoria, SUM(valor_unitario * quantidade) AS Valor_Vendido
FROM vendas
GROUP BY categoria
ORDER BY Valor_Vendido DESC;

-- EXERCÍCIO NÍVEL 3 - 14
SELECT categoria, SUM(quantidade) AS Quantidade_Vendida
FROM vendas
GROUP BY categoria
ORDER BY Quantidade_Vendida DESC;

-- EXERCÍCIO NÍVEL 3 - 15
SELECT estado, SUM(valor_unitario * quantidade) AS Valor_Vendido
FROM vendas
GROUP BY estado
ORDER BY Valor_Vendido DESC;

-- EXERCÍCIO NÍVEL 3 - 16
SELECT cliente, SUM(valor_unitario * quantidade) AS Valor_Vendido
FROM vendas
GROUP BY cliente
ORDER BY Valor_Vendido DESC;

-- EXERCÍCIO NÍVEL 3 - 17
SELECT cidade, SUM(quantidade) AS Quantidade_Vendida
FROM vendas
GROUP BY cidade
ORDER BY Quantidade_Vendida DESC;

-- EXERCÍCIO NÍVEL 3 - 18
SELECT categoria, AVG(valor_unitario) AS Valor_Medio_Unitario
FROM vendas
GROUP BY categoria
ORDER BY Valor_Medio_Unitario DESC;

-- EXERCÍCIO NÍVEL 4 - 19
SELECT categoria, SUM(valor_unitario * quantidade) AS Valor_Vendido
FROM vendas
GROUP BY categoria
HAVING Valor_Vendido > 10000
ORDER BY Valor_Vendido DESC;

-- EXERCÍCIO NÍVEL 4 - 20
SELECT cliente, SUM(valor_unitario * quantidade) AS Valor_Vendido
FROM vendas
GROUP BY cliente
HAVING Valor_Vendido > 5000
ORDER BY Valor_Vendido DESC;

-- EXERCÍCIO NÍVEL 4 - 21
SELECT estado, SUM(quantidade) AS Quantidade_Vendida
FROM vendas
GROUP BY estado
HAVING Quantidade_Vendida > 3
ORDER BY Quantidade_Vendida DESC;

-- EXERCÍCIO NÍVEL 4 - 22
SELECT categoria, SUM(quantidade) AS Quantidade_Vendida
FROM vendas
GROUP BY categoria
HAVING Quantidade_Vendida > 5
ORDER BY Quantidade_Vendida DESC;

-- EXERCÍCIO NÍVEL 4 - 23
SELECT cliente, SUM(quantidade) AS Quantidade_Vendida
FROM vendas
GROUP BY cliente
HAVING Quantidade_Vendida > 2
ORDER BY Quantidade_Vendida DESC;

-- EXERCÍCIO NÍVEL 5 - 24
SELECT c.categoria, max(c.Valor_Vendido)
FROM
(
SELECT categoria, SUM(valor_unitario * quantidade) AS Valor_Vendido
FROM vendas
GROUP BY categoria
) c

-- EXERCÍCIO NÍVEL 5 - 25
SELECT cli.cliente, cli.Valor_Vendido
FROM
(
SELECT cliente, SUM(valor_unitario * quantidade) AS Valor_Vendido
FROM vendas
GROUP BY cliente
ORDER BY Valor_Vendido DESC
) cli
LIMIT 1;
