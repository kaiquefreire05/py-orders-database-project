import tkinter as tk
from views.item.item_view import ItemView
from views.pedido.pedido_view import PedidoView


class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Pedidos")  # Define o título da janela principal

        self.root.geometry("400x400")  # Define o tamanho da janela principal

        tk.Label(self.root, text="Bem-vindo ao Sistema de Pedidos").pack(pady=20)  # Adiciona um rótulo de boas-vindas

        # Botão para abrir a janela de registro de itens
        tk.Button(self.root, text="Opções de itens", command=self.open_item_window).pack(pady=10)
        # Botão para abrir a janela de registro de pedidos
        tk.Button(self.root, text="Opções de pedido", command=self.open_pedido_window).pack(pady=10)

    def open_item_window(self):
        self.root.withdraw()  # Oculta a janela principal
        item_window = tk.Toplevel(self.root)  # Cria uma nova janela de nível superior
        # Inicializa a visão de item com a nova janela e a referência da janela principal
        ItemView(item_window, self.root)

    def open_pedido_window(self):
        self.root.withdraw()  # Oculta a janela principal
        pedido_window = tk.Toplevel(self.root)  # Cria uma nova janela de nível superior
        # Inicializa a visão de pedido com a nova janela e a referência da janela principal
        PedidoView(pedido_window, self.root)


