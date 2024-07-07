import tkinter as tk
from tkinter import messagebox
from controllers.item_controller import ItemController
from models.item import Item


class CadastroItemView:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.root.title("Cadastro de itens")  # Mudando título da janela
        self.root.geometry("400x400")  # Mudando o tamanho da janela

        self.item_controller = ItemController()  # Inicializa o controlador de itens
        self.create_widgets()  # Cria os widgets na janela

    def create_widgets(self):
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
        try:
            # Obtendo os valores
            nome = self.entrada_nome.get()
            descricao = self.entrada_desc.get()
            preco = float(self.entrada_preco.get())
            qtde = int(self.entrada_qtde.get())

            item = Item(nome=nome, descricao=descricao, preco=preco, quantidade=qtde)
            self.item_controller.cadastrar_item(item)
            messagebox.showinfo("Sucesso!", "Item cadastrado com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Digite os valores nos campos corretamente")

    def voltar(self):
        self.root.destroy()  # Fecha a janela de registro de item
        self.main_root.deiconify()  # Reexibe a janela principal
