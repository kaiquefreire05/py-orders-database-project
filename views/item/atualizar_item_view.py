from controllers.item_controller import ItemController
import tkinter as tk


class AtualizarItemView:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.item_controller = ItemController()
        self.root.title("Atualizar item")
        self.root.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        # item.nome, item.descricao, item.preco, item.quantidade

        # Configurando o grid para ter alinhamento
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Labels e entradas
        tk.Label(self.root, text="Id do Item:").grid(row=0, column=0, sticky='e', padx=10, pady=5)
        self.entrada_id = tk.Entry(self.root)
        self.entrada_id.grid(row=0, column=1, sticky='w', padx=10, pady=5)

        tk.Label(self.root, text="Nome:").grid(row=1, column=0, sticky='e', padx=10, pady=10)
        self.entrada_nome = tk.Entry(self.root)
        self.entrada_nome.grid(row=1, column=1, sticky='w', padx=10, pady=5)

        tk.Label(self.root, text="Descrição:").grid(row=2, column=0, sticky='e', padx=10, pady=5)
        self.entrada_desc = tk.Entry(self.root)

        
        # Botões
