import sqlite3
from database.orders_db import Database
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from controllers.item_controller import ItemController


class PedidoController:
    """
        Controller para operações relacionadas a pedidos e itens de pedido no banco de dados.
    """
    def __init__(self):
        """
            Inicializa o controlador com uma instância do banco de dados e do controlador de itens.
        """
        self.db = Database()
        self.item_controller = ItemController()

    def registrar_pedido(self, pedido, itens):
        """
            Registra um novo pedido e seus itens no banco de dados.

            Args:
                pedido (Pedido): Objeto Pedido contendo os dados do pedido.
                itens (list): Uma lista de objetos ItemPedido contendo os itens do pedido.

            Raises:
                ValueError: Se algum item do pedido não existir ou a quantidade for insuficiente.

        """

        # Query para inserir o pedido
        query_pedido = ('''
            INSERT INTO pedidos (data_pedido)
            VALUES (?)
            ''')

        params_pedido = (pedido.data_pedido,)
        self.db.execute_query(query_pedido, params_pedido)

        pedido_id = self.db.cursor.lastrowid

        # Query para inserir itens
        query_item_pedido = ('''
                    INSERT INTO itens_pedido (pedido_id, produto_id, quantidade)
                    VALUES (?, ?, ?)
                    ''')

        # Query para atualizar a quantidade de itens
        query_update_item = '''
                    UPDATE itens
                    SET quantidade = quantidade - ?
                    WHERE id = ? AND quantidade >= ?
                '''

        # Iterando sobre todos os itens
        for item in itens:
            # Verificando se o item existe na tabela de itens
            item_data = self.item_controller.obter_item(item.item_id)
            if not item_data or item_data[0][4] < item.quantidade:  # [0][4] local da quantidade
                raise ValueError(f'Item com ID {item.item_id} não existe ou quantidade insuficiente.')

            # Inserindo o item do pedido
            params_item = (pedido_id, item.item_id, item.quantidade)
            self.db.execute_query(query_item_pedido, params_item)

            # Atualizando a quantidade do item no estoque
            params_update_item = (item.quantidade, item.item_id, item.quantidade)
            self.db.execute_query(query_update_item, params_update_item)

    def excluir_pedido(self, id):
        """
            Exclui um pedido e seus itens do banco de dados.

            Args:
                id (int): O ID do pedido a ser excluído.

            Returns:
                bool: True se o pedido foi excluído com sucesso, False se não foi encontrado.

        """
        # Excluindo na tabela itens de pedido
        query_itens_pedido = 'DELETE FROM itens_pedido WHERE pedido_id = ?'
        self.db.execute_query(query_itens_pedido, (id,))

        # Excluindo na tabela pedido
        query_delete_pedido = 'DELETE FROM pedidos WHERE id = ?'
        # Usando nova função que executa o query, mas também retorna o número de linhas afetadas
        pedidos_afetados = self.db.execute_query_with_affected_rows(query_delete_pedido, (id,))

        return pedidos_afetados > 0  # True ou False

    def listar_pedidos(self):
        """
            Lista todos os pedidos cadastrados no banco de dados.

            Returns:
                list: Uma lista de tuplas contendo os dados de cada pedido e seus itens.

        """
        query = ('''
            SELECT p.id, p.data_pedido, ip.produto_id, ip.quantidade
            FROM pedidos p
            JOIN itens_pedido ip ON p.id = ip.pedido_id
            ''')
        return self.db.fetch_all(query)

    def atualizar_pedido(self, id, pedido, itens):
        """
            Atualiza um pedido e seus itens no banco de dados.

            Args:
                id (int): O ID do pedido a ser atualizado.
                pedido (Pedido): Objeto Pedido com os novos dados do pedido.
                itens (list): Uma lista de objetos ItemPedido com os novos itens do pedido.

        """

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
        """
            Carrega um pedido do banco de dados pelo seu ID.

            Args:
                id (int): O ID do pedido a ser carregado.

            Returns:
                tuple: Um objeto Pedido e uma lista de tuplas contendo os itens do pedido (produto_id, quantidade).

        """
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

