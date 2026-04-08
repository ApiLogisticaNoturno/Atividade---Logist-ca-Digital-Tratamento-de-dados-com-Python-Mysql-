SELECT * FROM ItensPedido;

SELECT 
p.PedidoID,
c.NomeCliente,
pr.NomeProduto,
ip.Quantidade,
t.NomeTransportadora,
p.StatusEntrega
FROM Pedidos p
JOIN Clientes c ON p.ClienteID = c.ClienteID
JOIN ItensPedido ip ON p.PedidoID = ip.PedidoID
JOIN Produtos pr ON ip.ProdutoID = pr.ProdutoID
JOIN Transportadoras t ON p.TransportadoraID = t.TransportadoraID;

/* Transportadora com mais entregas */
SELECT 
t.NomeTransportadora,
COUNT(*) AS TotalEntregas
FROM Pedidos p
JOIN Transportadoras t 
ON p.TransportadoraID = t.TransportadoraID
GROUP BY t.NomeTransportadora
ORDER BY TotalEntregas DESC;

/* Tempo médio de entrega */
SELECT 
AVG(DATEDIFF(DataEntregaReal, DataEnvio)) AS TempoMedioEntrega
FROM Pedidos;

/* Frete médio por transportadora */
SELECT 
t.NomeTransportadora,
AVG(p.CustoFrete) AS FreteMedio
FROM Pedidos p
JOIN Transportadoras t 
ON p.TransportadoraID = t.TransportadoraID
GROUP BY t.NomeTransportadora;
