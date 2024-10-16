
ItensDict = dict[str, int]

PedidoDict = dict[str, dict | str]

PedidosDict = dict[int, PedidoDict]

pedidos: PedidosDict = {
    213: {'destino': "Caicó",
          'itens': {"Bota": 100, "Sandália": 100},
          'entrega': "25/07/2024"},
    214: {'destino': "Natal",
          'itens': {"Bota": 200}},
    215: {'destino': "Natal",
          'itens': {"Sandália": 30, "Tênis": 40}},
    216: {'destino': "Caicó",
          'itens': {"Sandália": 20, "Tênis": 40}},
}
