class ItemPedido:
    """
    Representa um item dentro de um pedido com seu ID, quantidade e data do pedido.

    Attributes:
        item_id (int): ID do item associado ao pedido.
        quantidade (int): Quantidade do item no pedido.
        data_pedido (str): Data em que o pedido foi realizado.
    """

    def __init__(self, item_id, quantidade, data_pedido):
        """
        Inicializa um novo objeto ItemPedido.

        Args:
            item_id (int): ID do item associado ao pedido.
            quantidade (int): Quantidade do item no pedido.
            data_pedido (str): Data em que o pedido foi realizado.
        """
        self.item_id = item_id
        self.quantidade = quantidade
        self.data_pedido = data_pedido

    def __str__(self):
        """
        Retorna uma representação em string do objeto ItemPedido.

        Returns:
            str: String formatada com os atributos do item pedido.
        """
        return f'Pedido: Item_ID: {self.item_id}, Quantidade: {self.quantidade}, Data do Pedido: {self.data_pedido}'
