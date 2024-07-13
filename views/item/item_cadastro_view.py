import tkinter as tk
from tkinter import messagebox
from controllers.item_controller import ItemController
from models.item import Item


def validacao_campos_especifica(nome, desc, preco, qtde):
    """
        Valida os campos específicos para cadastro de item.

        Verifica se o nome e a descrição não estão vazios.
        Verifica se o preço pode ser convertido para float.
        Verifica se a quantidade pode ser convertida para inteiro.

        Args:
            nome (str): Nome do item.
            desc (str): Descrição do item.
            preco (str): Preço do item.
            qtde (str): Quantidade do item.

        Returns:
            tuple: Tupla contendo os valores válidos para nome, descrição, preço e quantidade.

        Raises:
            ValueError: Se nome ou descrição estiverem vazios.
            ValueError: Se preço não puder ser convertido para float.
            ValueError: Se quantidade não puder ser convertida para inteiro.
    """

    # Validando as strings
    if not nome or not desc:
        raise ValueError("Nome e descrição não podem estar vazios.")

    # Validando o preço (int)
    try:
        preco = float(preco)
    except ValueError:
        raise ValueError("Preço deve ser um número")

    # Validando a quantidade (float)
    try:
        qtde = int(qtde)
    except ValueError:
        raise ValueError("Quantidade deve ser um número inteiro")

    return nome, desc, preco, qtde


class CadastroItemView:
    """
        Classe para criar uma interface gráfica de cadastro de itens.

        Attributes:
            root (tk.TK): A janela raiz para a visualização de cadastro de itens.
            main_root (tk.TK): Referência à janela principal da aplicação.
            item_controller (ItemController): O controlador para gerenciar dados de item.
    """
    def __init__(self, root, main_root):
        """
            Inicializa a instância CadastroItemView.

            Args:
                root (tk.TK): A janela raiz para a visualização de cadastro de itens.
                main_root (tk.TK): Referência à janela principal da aplicação.
        """
        self.root = root
        self.main_root = main_root
        self.root.title("Cadastro de itens")  # Mudando título da janela
        self.root.geometry("600x500")  # Mudando o tamanho da janela

        self.item_controller = ItemController()  # Inicializa o controlador de itens
        self.create_widgets()  # Cria os widgets na janela

    def create_widgets(self):
        """
            Cria os widgets para a visualização de cadastro de itens.

            Este método configura o layout em grid e cria rótulos, campos de entrada e botões para interação do usuário.
        """

        # Configurando o grid para ter preenchimento e alinhamento
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Labels e entradas
        tk.Label(self.root, text="Nome do item").grid(row=0, column=0, sticky='e', padx=10, pady=5)
        self.entrada_nome = tk.Entry(self.root)
        self.entrada_nome.grid(row=0, column=1, sticky='w', padx=10, pady=5)

        tk.Label(self.root, text="Descrição").grid(row=1, column=0, sticky='e', padx=10, pady=5)
        self.entrada_desc = tk.Entry(self.root)
        self.entrada_desc.grid(row=1, column=1, sticky='w', padx=10, pady=5)

        tk.Label(self.root, text="Preço").grid(row=2, column=0, sticky='e', padx=10, pady=5)
        self.entrada_preco = tk.Entry(self.root)
        self.entrada_preco.grid(row=2, column=1, sticky='w', padx=10, pady=5)

        tk.Label(self.root, text="Quantidade").grid(row=3, column=0, sticky='e', padx=10, pady=5)
        self.entrada_qtde = tk.Entry(self.root)
        self.entrada_qtde.grid(row=3, column=1, sticky='w', padx=10, pady=5)

        # Botões
        tk.Button(self.root, text="Cadastrar item", command=self.cadastrar_item).grid(row=4, column=0, columnspan=2,
                                                                                      pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=5, column=0, columnspan=2)

    def cadastrar_item(self):
        """
            Tenta cadastrar um item com base nos valores inseridos pelo usuário.

            Obtém os valores dos campos de entrada, valida-os utilizando a função (validacao_campos_especifica),
            cria uma instância de (Item) e chama o método (cadastrar_item) do controlador de itens.
            Exibe uma mensagem de sucesso se o item for cadastrado com sucesso.
            Em caso de erro, exibe uma mensagem de erro correspondente.
        """
        # Obtendo os valores
        nome = self.entrada_nome.get()
        descricao = self.entrada_desc.get()
        preco = self.entrada_preco.get()
        qtde = self.entrada_qtde.get()

        try:
            nome, descricao, preco, qtde = validacao_campos_especifica(nome, descricao, preco, qtde)
            item = Item(nome=nome, descricao=descricao, preco=preco, quantidade=qtde)
            self.item_controller.cadastrar_item(item)
            messagebox.showinfo("Sucesso", "Item foi cadastrado com sucesso!")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def voltar(self):
        """
            Retorna à janela anterior da aplicação.

            Este método fecha a janela de cadastro de item e torna visível novamente a janela principal da aplicação.
        """
        self.root.destroy()  # Fecha a janela de registro de item
        self.main_root.deiconify()  # Reexibe a janela principal
