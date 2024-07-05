class ItemPedido:
    def __init__(self, item_id, quantidade, data_pedido):
        self.item_id = item_id
        self.quantidade = quantidade
        self.data_pedido = data_pedido

    def __str__(self):
        return f'Pedido: Item_ID: {self.item_id}, Quantidade: {self.quantidade}, Data do Pedido: {self.data_pedido}'
