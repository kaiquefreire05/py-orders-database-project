class Item:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f'Nome: {self.nome}, Descrição: {self.descricao}, Preço: {self.preco}, Quantidade: {self.quantidade}'
