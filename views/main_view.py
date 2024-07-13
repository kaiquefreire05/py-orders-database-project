import tkinter as tk
from views.item.item_view import ItemView
from views.pedido.pedido_view import PedidoView


class MainView:
    """
    Classe para gerenciar a interface gráfica principal do sistema de pedidos.

    Attributes:
        root (tk.TK): Janela principal da aplicação.
    """

    def __init__(self, root):
        """
        Inicializa a janela principal e os botões para acessar as funcionalidades de itens e pedidos.

        Args:
            root (tk.TK): Janela principal da aplicação.
        """
        self.root = root
        self.root.title("Sistema de Pedidos")  # Define o título da janela principal
        self.root.geometry("400x400")  # Define o tamanho da janela principal

        tk.Label(self.root, text="Bem-vindo ao Sistema de Pedidos").pack(pady=20)  # Rótulo de boas-vindas

        # Botão para abrir a janela de registro de itens
        tk.Button(self.root, text="Opções de itens", command=self.open_item_window).pack(pady=10)
        # Botão para abrir a janela de registro de pedidos
        tk.Button(self.root, text="Opções de pedido", command=self.open_pedido_window).pack(pady=10)

    def open_item_window(self):
        """
        Abre uma nova janela para exibir as opções de itens.

        Oculta a janela principal e cria uma nova janela de nível superior para a visualização de itens.
        """
        self.root.withdraw()  # Oculta a janela principal
        item_window = tk.Toplevel(self.root)  # Cria uma nova janela de nível superior
        ItemView(item_window, self.root)

    def open_pedido_window(self):
        """
        Abre uma nova janela para exibir as opções de pedidos.

        Oculta a janela principal e cria uma nova janela de nível superior para a visualização de pedidos.
        """
        self.root.withdraw()  # Oculta a janela principal
        pedido_window = tk.Toplevel(self.root)  # Cria uma nova janela de nível superior
        PedidoView(pedido_window, self.root)
