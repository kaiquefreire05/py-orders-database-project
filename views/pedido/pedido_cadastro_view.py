import tkinter as tk
from controllers.pedido_controller import PedidoController
from tkinter import messagebox
from models.pedido import Pedido
from models.item_pedido import ItemPedido


class CadastroPedidoView:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.pedido_controller = PedidoController()
        self.root.title("Cadastro de Pedido")
        self.root.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        tk.Label(self.root, text="Data do Pedido").grid(row=0, column=0, stick='e', padx=10, pady=5)
        self.entry_data_pedido = tk.Entry(self.root)
        self.entry_data_pedido.grid(row=0, column=1, stick='w', padx=10, pady=5)

        tk.Label(self.root, text="Item ID").grid(row=1, column=0, stick='e', padx=10, pady=5)
        self.entry_item_ids = tk.Entry(self.root)
        self.entry_item_ids.grid(row=1, column=1, stick='w', padx=10, pady=5)

        tk.Label(self.root, text="Quantidade").grid(row=2, column=0, stick='e', padx=10, pady=5)
        self.entry_quantidades = tk.Entry(self.root)
        self.entry_quantidades.grid(row=2, column=1, stick='w', padx=10, pady=5)

        tk.Button(self.root, text="Registrar Pedido", command=self.registrar_pedido).grid(row=3, column=0
                                                                                          , columnspan=2, pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=4, column=0, columnspan=2, pady=10)

    def registrar_pedido(self):
        # Obtém os valores dos campos de entrada
        data_pedido = self.entry_data_pedido.get()
        pedido = Pedido(data_pedido)

        item_ids = self.entry_item_ids.get().split(', ')
        quantidades = self.entry_quantidades.get().split(', ')

        # Verifica se as quantidades de IDs e quantidades são iguais
        if len(item_ids) != len(quantidades):
            messagebox.showerror("Erro", "O número de IDs de itens e quantidades não corresponde.")
            return

        # Cria uma lista de ItemPedido
        itens_pedido = []
        for item_id, quantidade in zip(item_ids, quantidades):
            try:
                item_id = int(item_id.strip())
                quantidade = int(quantidade.strip())
                item_pedido = ItemPedido(item_id, quantidade, data_pedido)
                itens_pedido.append(item_pedido)
            except ValueError:
                messagebox.showerror("Erro", "IDs de itens e quantidades devem ser números inteiros.")
                return

        # Registra o pedido
        self.pedido_controller.registrar_pedido(pedido, itens_pedido)
        messagebox.showinfo("Sucesso", "Pedido registrado com sucesso!")

    def voltar(self):
        self.root.destroy()  # Fecha a janela de registro de pedido
        self.main_root.deiconify()  # Reexibe a janela principal
