import sqlite3


class Database:
    """
        Classe para interação com o banco de dados SQLite.
    """

    def __init__(self, nome_db='orders.db'):
        """
            Inicializa a conexão com o banco de dados SQLite e cria as tabelas se elas não existirem.

            Args:
                nome_db (str): Nome do arquivo do banco de dados SQLite.

        """

        # Tentando conectar com o banco de dados
        try:
            self.connection = sqlite3.connect(nome_db)
        except sqlite3.DataError as e:  # Lançando o erro
            print('Ocorreu um erro na conexão do banco de dados. Erro: ', e)
        self.cursor = self.connection.cursor()  # Cursor para executar algum query
        self.create_tables()  # Criando as tabelas do banco de dados

    def create_tables(self):
        """
            Cria as tabelas do banco de dados se elas não existirem.
        """

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL
            )
            ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_pedido TEXT NOT NULL
            )
            ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens_pedido (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pedido_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                FOREIGN KEY (pedido_id) REFERENCES pedidos (id),
                FOREIGN KEY (produto_id) REFERENCES itens (id)
            )
            ''')
        self.connection.commit()  # Executando a mudança

    def execute_query(self, query, params=()):
        """
            Executa uma consulta SQL que não retorna resultados.

            Args:
                query (str): A consulta SQL a ser executada.
                params (tuple): Parâmetros para substituição na consulta SQL.

        """
        self.cursor.execute(query, params)
        self.connection.commit()  # Confirmando a alteração

    def execute_query_with_affected_rows(self, query, params=()):
        """
            Executa uma consulta SQL que retorna o número de linhas afetadas.

            Args:
                query (str): A consulta SQL a ser executada.
                params (tuple): Parâmetros para substituição na consulta SQL.

            Returns:
                int: Número de linhas afetadas pela consulta.

        """

        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.rowcount  # Retornando com o número de linhas afetadas

    def fetch_all(self, query, params=()):
        """
            Executa uma consulta SQL que retorna todas as linhas de resultado.

            Args:
                query (str): A consulta SQL a ser executada.
                params (tuple): Parâmetros para substituição na consulta SQL.

            Returns:
                list: Lista contendo todas as linhas de resultado da consulta.

        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self):
        """
            Fecha a conexão com o banco de dados.
        """
        self.connection.close()
