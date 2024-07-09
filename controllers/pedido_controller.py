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
        query_itens_pedido = 'DELETE FROM itens_pedido WHERE pedido_id = ?'
        self.db.execute_query(query_itens_pedido, (id,))

        # Excluindo na tabela pedido
        query_delete_pedido = 'DELETE FROM pedidos WHERE id = ?'
        # Usando nova função que executa o query, mas também retorna o número de linhas afetadas
        pedidos_afetados = self.db.execute_query_with_affected_rows(query_delete_pedido, (id,))

        return pedidos_afetados > 0

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

    def carrega_pedido(self, id):
        query_pedido = 'SELECT data_pedido FROM pedidos WHERE id = ?'
        pedido_data = self.db.fetch_all(query_pedido, (id,))

        # Se o pedido for vazio retornar None
        if not pedido_data:
            return None, None

        # Recuperando os itens
        query_itens = 'SELECT produto_id, quantidade FROM itens_pedido WHERE pedido_id = ?'
        itens_data = self.db.fetch_all(query_itens, (id,))

        # Assumindo que fetch_all retorna uma lista de tuplas
        if pedido_data:
            data_pedido = pedido_data[0][0]  # Acessa o primeiro elemento da primeira tupla
            pedido = Pedido(data_pedido=data_pedido)
            itens = [(item[0], item[1]) for item in itens_data]
            return pedido, itens
        return None, None

