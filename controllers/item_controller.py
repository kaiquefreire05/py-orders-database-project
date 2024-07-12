import sqlite3

from database.orders_db import Database
from models.item import Item


class ItemController:
    def __init__(self):
        self.db = Database()  # Instânciando o banco de dados

    def cadastrar_item(self, item):
        query = ('''
        INSERT INTO itens (nome, descricao, preco, quantidade)
        VALUES (?, ?, ?, ?)
        ''')

        params = (item.nome, item.descricao, item.preco, item.quantidade)
        self.db.execute_query(query, params)
        print(f'Item cadastrado com sucesso.')

    def listar_todos(self):
        query = ('''
        SELECT * FROM itens
        ''')
        return self.db.fetch_all(query)

    def atualizar_item(self, id, item):
        query = ('''
        UPDATE itens
        SET nome = ?, descricao = ?, preco = ?, quantidade = ?
        WHERE id = ?
        ''')
        params = (item.nome, item.descricao, item.preco, item.quantidade, id)

        self.db.execute_query(query, params)
        print('Item foi atualizado com sucesso!')

    def excluir_item(self, id):
        query = 'DELETE FROM itens WHERE id = ?'
        self.db.execute_query(query, (id,))

    def obter_item(self, item_id):
        query = 'SELECT * FROM itens WHERE id = ?'
        return self.db.fetch_all(query, (item_id,))
