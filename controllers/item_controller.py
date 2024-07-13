import sqlite3
from database.orders_db import Database
from models.item import Item


class ItemController:
    """
        Controller para operações CRUD de itens no banco de dados.
    """
    def __init__(self):
        """
            Inicializa o controlador com uma instância do banco de dados.
        """
        self.db = Database()  # Instânciando o banco de dados

    def cadastrar_item(self, item):
        """
            Cadastra um novo item no banco de dados.

            Args:
                item (Item): O objeto Item a ser cadastrado.

        """

        query = ('''
        INSERT INTO itens (nome, descricao, preco, quantidade)
        VALUES (?, ?, ?, ?)
        ''')

        params = (item.nome, item.descricao, item.preco, item.quantidade)
        self.db.execute_query(query, params)
        print(f'Item cadastrado com sucesso.')

    def listar_todos(self):
        """
            Lista todos os itens cadastrados no banco de dados.

            Returns:
                list: Uma lista de tuplas contendo os dados de cada item.

        """

        query = ('''
        SELECT * FROM itens
        ''')
        return self.db.fetch_all(query)

    def atualizar_item(self, id, item):
        """
            Atualiza um item existente no banco de dados.

            Args:
                id (int): O ID do item a ser atualizado.
                item (Item): O objeto Item com os novos dados.

        """

        query = ('''
        UPDATE itens
        SET nome = ?, descricao = ?, preco = ?, quantidade = ?
        WHERE id = ?
        ''')
        params = (item.nome, item.descricao, item.preco, item.quantidade, id)

        self.db.execute_query(query, params)

    def excluir_item(self, id):
        """
            Exclui um item do banco de dados.

            Args:
                id (int): O ID do item a ser excluído.

            Returns:
                bool: True se o item foi excluído com sucesso, False se não foi encontrado.

        """

        query = 'DELETE FROM itens WHERE id = ?'
        linhas_afetadas = self.db.execute_query_with_affected_rows(query, (id,))
        return linhas_afetadas > 0  # Se não foi afetada nenhuma linha return False

    def obter_item(self, item_id):
        """
            Obtém um item do banco de dados pelo seu ID.

            Args:
                item_id (int): O ID do item a ser obtido.

            Returns:
                list: Uma lista de tuplas contendo os dados do item encontrado.

        """

        query = 'SELECT * FROM itens WHERE id = ?'
        return self.db.fetch_all(query, (item_id,))
