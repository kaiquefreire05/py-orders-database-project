import tkinter as tk
from views.pedido.pedido_cadastro_view import CadastroPedidoView
from views.pedido.mostrar_pedidos_view import MostrarPedidosView
from views.pedido.exclui_pedido_view import ExcluiPedidoView
from views.pedido.atualiza_pedido_view import AtualizaPedidoView


class PedidoView:
    """
    Classe para gerenciar a interface gráfica principal de pedidos.

    Attributes:
        root (tk.Tk): Janela principal da aplicação.
        main_root (tk.Tk): Janela principal anterior à abertura desta interface.
    """

    def __init__(self, root, main_root):
        """
        Inicializa a janela principal da interface de pedidos.

        Args:
            root (tk.Tk): Janela principal da aplicação.
            main_root (tk.Tk): Janela principal anterior à abertura desta interface.
        """
        self.root = root
        self.main_root = main_root
        self.root.title("Registrar Pedido")  # Define o título da janela de registro de pedido
        self.root.geometry("600x500")  # Define o tamanho da janela de registro de pedido
        self.create_widgets()  # Cria os widgets na janela

    def create_widgets(self):
        """
        Cria os widgets (botões) na janela principal para acessar as funcionalidades relacionadas a pedidos.
        """
        tk.Button(self.root, text="Registrar pedido", command=self.open_registro_pedido).pack(pady=10)
        tk.Button(self.root, text="Mostrar pedido", command=self.open_mostra_pedido).pack(pady=10)
        tk.Button(self.root, text="Excluir pedido", command=self.open_exclui_pedido).pack(pady=10)
        tk.Button(self.root, text="Atualizar pedido", command=self.open_atualiza_pedido).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).pack(pady=10)

    def voltar(self):
        """
        Fecha a janela atual de registro de pedido e reexibe a janela principal anterior.
        """
        self.root.destroy()  # Fecha a janela de registro de pedido
        self.main_root.deiconify()  # Reexibe a janela principal

    def open_registro_pedido(self):
        """
        Abre uma nova janela para registrar um novo pedido.
        """
        self.root.withdraw()
        pedido_window = tk.Toplevel(self.root)
        CadastroPedidoView(pedido_window, self.root)

    def open_mostra_pedido(self):
        """
        Abre uma nova janela para mostrar todos os pedidos registrados.
        """
        self.root.withdraw()
        pedido_window = tk.Toplevel(self.root)
        MostrarPedidosView(pedido_window, self.root)

    def open_exclui_pedido(self):
        """
        Abre uma nova janela para excluir um pedido existente.
        """
        self.root.withdraw()
        pedido_window = tk.Toplevel(self.root)
        ExcluiPedidoView(pedido_window, self.root)

    def open_atualiza_pedido(self):
        """
        Abre uma nova janela para atualizar um pedido existente.
        """
        self.root.withdraw()
        pedido_window = tk.Toplevel(self.root)
        AtualizaPedidoView(pedido_window, self.root)
