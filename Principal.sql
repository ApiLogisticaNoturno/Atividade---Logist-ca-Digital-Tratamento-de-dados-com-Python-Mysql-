/*CREATE DATABASE logistica;
USE logistica;*/

CREATE TABLE Clientes (
ClienteID VARCHAR(10) PRIMARY KEY,
NomeCliente VARCHAR(100),
Cidade VARCHAR(100),
UF CHAR(2),
Latitude DECIMAL(9,6),
Longitude DECIMAL(9,6)
);

CREATE TABLE Produtos (
ProdutoID INT PRIMARY KEY,
NomeProduto VARCHAR(100),
CategoriaProduto VARCHAR(50)
);

CREATE TABLE Transportadoras (
TransportadoraID INT PRIMARY KEY,
NomeTransportadora VARCHAR(100)
);

CREATE TABLE Pedidos (
PedidoID INT PRIMARY KEY,
ClienteID VARCHAR(10),
TransportadoraID INT,
DataPedido DATE,
DataEnvio DATE,
DataEntregaPrevista DATE,
DataEntregaReal DATE,
StatusEntrega VARCHAR(50),
CustoFrete DECIMAL(10,2),
DistanciaKM DECIMAL(10,2),
AvaliacaoCliente INT,
CodigoRastreio VARCHAR(20),
PesoKG DECIMAL(10,2),
TipoTransporte VARCHAR(20),
PrioridadeEntrega VARCHAR(20),
StatusPagamento VARCHAR(20),
DataPagamento DATETIME,
FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
FOREIGN KEY (TransportadoraID) REFERENCES Transportadoras(TransportadoraID)
);

CREATE TABLE ItensPedido (
ItemID INT AUTO_INCREMENT PRIMARY KEY,
PedidoID INT,
ProdutoID INT,
Quantidade INT,
ValorUnitario DECIMAL(10,2),
FOREIGN KEY (PedidoID) REFERENCES Pedidos(PedidoID),
FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);