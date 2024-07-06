from controllers.item_controller import ItemController
import tkinter as tk
from tkinter import messagebox
from models.item import Item


class AtualizarItemView:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.item_controller = ItemController()
        self.root.title("Atualizar item")
        self.root.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):

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
        self.root.destroy()
        self.main_root.deiconify()
