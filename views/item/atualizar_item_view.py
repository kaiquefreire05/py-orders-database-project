from controllers.item_controller import ItemController
import tkinter as tk
from tkinter import messagebox
from models.item import Item


class AtualizarItemView:
    """
        Classe para criar uma interface gráfica para atualizar itens.

        Atributos:
            root (tk.TK): A janela principal para a visualização de atualização de item.
            main_root (tk.TK): Referência à janela principal da aplicação.
            item_controller (ItemController): O controlador para gerenciar dados de item.
    """
    def __init__(self, root, main_root):
        """
            Inicializa a instância AtualizarItemView.

            Args:
                root (tk.TK): A janela principal para a visualização de atualização de item.
                main_root (tk.TK): Referência à janela principal da aplicação.
        """
        self.root = root
        self.main_root = main_root
        self.item_controller = ItemController()  # Controlador dos itens
        self.root.title("Atualizar item")
        self.root.geometry("600x500")
        self.create_widgets()

    def create_widgets(self):
        """
            Cria os widgets para a visualização de atualização de item.

            Este método configura o layout em grid e cria rótulos, campos de entrada e botões para interação do usuário.
        """

        # Configurando o grid para ter alinhamento
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # ID
        tk.Label(self.root, text="Id do Item:").grid(row=0, column=0, sticky='e', padx=10, pady=5)
        self.entrada_id = tk.Entry(self.root)
        self.entrada_id.grid(row=0, column=1, sticky='w', padx=10, pady=5)

        # Nome
        tk.Label(self.root, text="Nome:").grid(row=1, column=0, sticky='e', padx=10, pady=10)
        self.entrada_nome = tk.Entry(self.root)
        self.entrada_nome.grid(row=1, column=1, sticky='w', padx=10, pady=5)

        # Descrição
        tk.Label(self.root, text="Descrição:").grid(row=2, column=0, sticky='e', padx=10, pady=5)
        self.entrada_desc = tk.Entry(self.root)
        self.entrada_desc.grid(row=2, column=1, sticky='w', padx=10, pady=5)

        # Preço
        tk.Label(self.root, text="Preço:").grid(row=3, column=0, sticky='e', padx=10, pady=5)
        self.entrada_preco = tk.Entry(self.root)
        self.entrada_preco.grid(row=3, column=1, sticky='w')

        # Quantidade
        tk.Label(self.root, text="Quantidade:").grid(row=4, column=0, sticky='e', padx=10, pady=5)
        self.entrada_qtde = tk.Entry(self.root)
        self.entrada_qtde.grid(row=4, column=1, sticky='w')

        # Botões
        tk.Button(self.root, text="Clique aqui para atualizar o item", command=self.atualizar_item).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=6, column=0, columnspan=2)

    def atualizar_item(self):
        """
            Tenta atualizar um item com base na entrada do usuário.

            Este método recupera dados dos campo de entrada, valida-os e chama o (ItemController) para atualizar o item.
            Em caso de erros, exibe uma mensagem de erro.
        """
        try:
            id = int(self.entrada_id.get())
            nome = self.entrada_nome.get()
            desc = self.entrada_desc.get()
            preco = float(self.entrada_preco.get())
            qtde = int(self.entrada_qtde.get())

            item_atualizado = Item(nome=nome, descricao=desc, preco=preco, quantidade=qtde)
            self.item_controller.atualizar_item(id, item_atualizado)
            messagebox.showinfo("Sucesso!", "item atualizado com sucesso!")
        except ValueError:
            messagebox.showerror("Erro!", "Insira valores válidos nos campos!")

    def voltar(self):
        """
            Retorna à janela anterior da aplicação.

            Este método fecha a janela atual e torna visível novamente a janela principal da aplicação.
        """
        self.root.destroy()
        self.main_root.deiconify()
