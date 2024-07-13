class Pedido:
    """
    Representa um pedido com sua data de realização.

    Attributes:
        data_pedido (str): Data em que o pedido foi realizado.
    """

    def __init__(self, data_pedido):
        """
        Inicializa um novo objeto Pedido com a data do pedido.

        Args:
            data_pedido (str): Data em que o pedido foi realizado.
        """
        self.data_pedido = data_pedido
