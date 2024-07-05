import sqlite3


class Database:
    def __init__(self, nome_db='orders.db'):

        # Tentando conectar com o banco de dados
        try:
            self.connection = sqlite3.connect(nome_db)
        except sqlite3.DataError as e:  # Lançando o erro
            print('Ocorreu um erro na conexão do banco de dados. Erro: ', e)
        self.cursor = self.connection.cursor()  # Cursor para executar algum query
        self.create_tables()  # Criando as tabelas do banco de dados

    def create_tables(self):
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

        self.cursor.execute(query, params)
        self.connection.commit()  # Confirmando a alteração

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
