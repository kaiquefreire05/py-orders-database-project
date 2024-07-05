import sqlite3

from database.orders_db import Database
from models.pedido import Pedido
from models.item_pedido import ItemPedido


class PedidoController:
    def __init__(self):
        self.db = Database()

    def registrar_pedido(self, pedido, itens):
        query_pedido = ('''
            INSERT INTO pedidos (data_pedido)
            VALUES (?)
            ''')

        params_pedido = (pedido.data_pedido,)
        self.db.execute_query(query_pedido, params_pedido)

        pedido_id = self.db.cursor.lastrowid

        query_item_pedido = ('''
                    INSERT INTO itens_pedido (pedido_id, produto_id, quantidade)
                    VALUES (?, ?, ?)
                    ''')

        for item in itens:
            params_item = (pedido_id, item.item_id, item.quantidade)
            self.db.execute_query(query_item_pedido, params_item)

    def excluir_pedido(self, id):
        # Excluindo na tabela itens de pedido

        query = 'DELETE FROM itens_pedido WHERE pedido_id = ?'
        self.db.execute_query(query, (id,))

        # Excluindo na tabela pedido
        query_delete_pedido = 'DELETE FROM pedidos WHERE id = ?'
        self.db.execute_query(query_delete_pedido, (id,))

    def listar_pedidos(self):

        query = ('''
            SELECT p.id, p.data_pedido, ip.produto_id, ip.quantidade
            FROM pedidos p
            JOIN itens_pedido ip ON p.id = ip.pedido_id
            ''')
        return self.db.fetch_all(query)

    def atualizar_pedido(self, id, pedido, itens):

        # Query para atualizar a data do pedido
        query_pedido = ('''
            UPDATE pedidos
            SET data_pedido = ?
            WHERE id = ?
            ''')

        # Atualizando a data do pedido
        params_pedido = (pedido.data_pedido, id)
        self.db.execute_query(query_pedido, params_pedido)

        # Deletando todos os itens do pedido com id passado por parâmetro
        query_delete_itens = 'DELETE FROM itens_pedido WHERE pedido_id = ?'  # Query para deletar os itens no pedido
        self.db.execute_query(query_delete_itens, (id,))

        # Query para inserir os itens no pedido
        query_item_pedido = ('''
            INSERT INTO itens_pedido (pedido_id, produto_id, quantidade)
            VALUES (?, ?, ?)
            ''')

        # Inserindo os novos itens
        for item in itens:
            params_item_pedido = (id, item.item_id, item.quantidade)
            self.db.execute_query(query_item_pedido, params_item_pedido)
