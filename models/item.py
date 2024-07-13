class Item:
    """
        Representa um item com nome, descrição, preço e quantidade.

        Attributes:
            nome (str): Nome do item.
            descricao (str): Descrição do item.
            preco (float): Preço do item.
            quantidade (int): Quantidade disponível do item.
    """
    def __init__(self, nome, descricao, preco, quantidade):
        """
            Inicializa um novo objeto Item.

            Args:
                nome (str): Nome do item.
                descricao (str): Descrição do item.
                preco (float): Preço do item.
                quantidade (int): Quantidade disponível do item.
        """
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        """
            Retorna uma representação em string do objeto Item.

            Returns:
                str: String formatada com os atributos do item.
        """

        return f'Nome: {self.nome}, Descrição: {self.descricao}, Preço: {self.preco}, Quantidade: {self.quantidade}'
