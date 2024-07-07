import tkinter as tk
from views.pedido.pedido_cadastro_view import CadastroPedidoView
from views.pedido.mostrar_pedidos_view import MostrarPedidosView
from views.pedido.exclui_pedido_view import ExcluiPedidoView
from views.pedido.atualiza_pedido_view import AtualizaPedidoView


class PedidoView:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.root.title("Registrar Pedido")  # Define o título da janela de registro de pedido
        self.root.geometry("400x400")  # Define o tamanho da janela de registro de pedido
        self.create_widgets()  # Cria os widgets na janela

    def create_widgets(self):
        tk.Button(self.root, text="Registrar pedido", command=self.open_registro_pedido).pack(pady=10)
        tk.Button(self.root, text="Mostrar pedido", command=self.open_mostra_pedido).pack(pady=10)
        tk.Button(self.root, text="Excluir pedido", command=self.open_exclui_pedido).pack(pady=10)
        tk.Button(self.root, text="Atualizar pedido", command=self.open_atualiza_pedido).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).pack(pady=10)

    def voltar(self):
        self.root.destroy()  # Fecha a janela de registro de pedido
        self.main_root.deiconify()  # Reexibe a janela principal

    def open_registro_pedido(self):
        self.root.withdraw()
        pedido_window = tk.Toplevel(self.root)
        CadastroPedidoView(pedido_window, self.root)

    def open_mostra_pedido(self):
        self.root.withdraw()
        pedido_window = tk.Toplevel(self.root)
        MostrarPedidosView(pedido_window, self.root)

    def open_exclui_pedido(self):
        self.root.withdraw()
        pedido_window = tk.Toplevel(self.root)
        ExcluiPedidoView(pedido_window, self.root)

    def open_atualiza_pedido(self):
        self.root.withdraw()
        pedido_window = tk.Toplevel(self.root)
        AtualizaPedidoView(pedido_window, self.root)

