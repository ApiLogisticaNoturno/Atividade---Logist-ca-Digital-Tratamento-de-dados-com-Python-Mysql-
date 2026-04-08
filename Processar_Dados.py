import pandas as pd

# Ler arquivo CSV
df = pd.read_csv("logistica_entregas_geo.csv.xls")

# -------------------------
# CLIENTES
# -------------------------
clientes = df[['ClienteID','NomeCliente','Cidade','UF','Latitude','Longitude']].drop_duplicates()

clientes_sql = []
for _, row in clientes.iterrows():
    sql = f"""INSERT INTO Clientes (ClienteID, NomeCliente, Cidade, UF, Latitude, Longitude)
VALUES ('{row.ClienteID}', '{row.NomeCliente}', '{row.Cidade}', '{row.UF}', {row.Latitude}, {row.Longitude});"""
    clientes_sql.append(sql)

# -------------------------
# PRODUTOS
# -------------------------
produtos = df[['Produto','CategoriaProduto']].drop_duplicates().reset_index(drop=True)
produtos['ProdutoID'] = produtos.index + 1

produtos_sql = []
for _, row in produtos.iterrows():
    sql = f"""INSERT INTO Produtos (ProdutoID, NomeProduto, CategoriaProduto)
VALUES ({row.ProdutoID}, '{row.Produto}', '{row.CategoriaProduto}');"""
    produtos_sql.append(sql)

# -------------------------
# TRANSPORTADORAS
# -------------------------
transportadoras = df[['Transportadora']].drop_duplicates().reset_index(drop=True)
transportadoras['TransportadoraID'] = transportadoras.index + 1

transportadoras_sql = []
for _, row in transportadoras.iterrows():
    sql = f"""INSERT INTO Transportadoras (TransportadoraID, NomeTransportadora)
VALUES ({row.TransportadoraID}, '{row.Transportadora}');"""
    transportadoras_sql.append(sql)

# -------------------------
# MAPEAR IDs
# -------------------------
map_produtos = dict(zip(produtos['Produto'], produtos['ProdutoID']))
map_transportadoras = dict(zip(transportadoras['Transportadora'], transportadoras['TransportadoraID']))

# -------------------------
# PEDIDOS
# -------------------------
pedidos_sql = []

for _, row in df.iterrows():

    transportadora_id = map_transportadoras[row.Transportadora]

    sql = f"""INSERT INTO Pedidos
(PedidoID, ClienteID, TransportadoraID, DataPedido, DataEnvio, DataEntregaPrevista,
DataEntregaReal, StatusEntrega, CustoFrete, DistanciaKM, AvaliacaoCliente,
CodigoRastreio, PesoKG, TipoTransporte, PrioridadeEntrega, StatusPagamento, DataPagamento)
VALUES
({row.PedidoID}, '{row.ClienteID}', {transportadora_id}, '{row.DataPedido}', '{row.DataEnvio}',
'{row.DataEntregaPrevista}', '{row.DataEntregaReal}', '{row.StatusEntrega}',
{row.CustoFrete}, {row.DistanciaKM}, {row.AvaliacaoCliente}, '{row.CodigoRastreio}',
{row.PesoKG}, '{row.TipoTransporte}', '{row.PrioridadeEntrega}',
'{row.StatusPagamento}', '{row.DataPagamento}');"""

    pedidos_sql.append(sql)

# -------------------------
# ITENS PEDIDO
# -------------------------
itens_sql = []

for _, row in df.iterrows():

    produto_id = map_produtos[row.Produto]

    sql = f"""INSERT INTO ItensPedido
(PedidoID, ProdutoID, Quantidade, ValorUnitario)
VALUES
({row.PedidoID}, {produto_id}, {row.Quantidade}, {row.ValorUnitario});"""

    itens_sql.append(sql)

# -------------------------
# SALVAR ARQUIVOS SQL
# -------------------------

with open("clientes.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(clientes_sql))

with open("produtos.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(produtos_sql))

with open("transportadoras.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(transportadoras_sql))

with open("pedidos.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(pedidos_sql))

with open("itens_pedido.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(itens_sql))

print("Arquivos SQL gerados com sucesso!")