import tkinter as tk
from controllers.pedido_controller import PedidoController


class MostrarPedidosView:
    """
        View para exibir todos os pedidos registrados.

        Attributes:
            root (tk.TK): Janela principal da aplicação.
            main_root (tk.TK): Referência à janela principal para retornar após fechar esta view.
            pedido_controller (PedidoController): Controlador de pedidos para interação com o modelo e banco de dados.
            list_box_pedidos (tk.Listbox): Widget Listbox para mostrar os pedidos e seus itens.
    """
    def __init__(self, root, main_root):
        """
            Inicializa a view de exibição de pedidos.

            Args:
                root (tk.TK): Janela principal da aplicação.
                main_root (tk.TK): Referência à janela principal para retornar após fechar esta view.
        """
        self.root = root
        self.main_root = main_root
        self.pedido_controller = PedidoController()
        self.root.title("Pedidos Registrados")
        self.root.geometry("600x500")
        self.create_widgets()

    def create_widgets(self):
        """
            Cria os widgets na janela de exibição de pedidos.
        """

        # Configurando colunas da interface
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        tk.Label(self.root, text="Clique no botão para mostrar todos os pedidos").grid(row=0, column=0, columnspan=3
                                                                                       , pady=10)
        tk.Button(self.root, text="Clique no botão para mostrar os pedidos"
                  , command=self.mostrar_pedidos).grid(row=1, column=1, pady=10)

        self.list_box_pedidos = tk.Listbox(self.root, width=60, height=10)
        self.list_box_pedidos.grid(row=3, column=0, columnspan=3, pady=10)

        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=5, column=1, pady=10)

    def mostrar_pedidos(self):
        """
        Mostra todos os pedidos na Listbox.
        """

        self.list_box_pedidos.delete(0, tk.END)  # Limpa a Listbox antes de exibir os novos pedidos

        pedidos = self.pedido_controller.listar_pedidos()  # Obtém todos os pedidos do controlador

        pedidos_dict = {}  # Dicionário para organizar os pedidos e seus itens
        for pedido in pedidos:
            pedido_id = pedido[0]  # ID do pedido
            data_pedido = pedido[1]  # Data do pedido

            # Se o pedido ainda não estiver no dicionário, adiciona uma nova entrada
            if pedido_id not in pedidos_dict:
                pedidos_dict[pedido_id] = {"data": data_pedido, "itens": []}

            # Adiciona o item ao pedido correspondente no dicionário
            pedidos_dict[pedido_id]["itens"].append(pedido[2:])

        # Itera sobre o dicionário de pedidos para exibir na Listbox
        for pedido_id, pedido_info in pedidos_dict.items():
            self.list_box_pedidos.insert(tk.END, f"Pedido ID: {pedido_id}, Data: {pedido_info['data']}")

            # Exibe todos os itens do pedido na Listbox
            for item in pedido_info["itens"]:
                cod_item, quantidade = item
                self.list_box_pedidos.insert(tk.END, f"  Item ID: {cod_item}, Quantidade: {quantidade}")

            self.list_box_pedidos.insert(tk.END, "")  # Linha em branco para separar os pedidos

    def voltar(self):
        """
        Fecha a janela de exibição de pedidos e retorna à janela anterior.
        """
        self.root.destroy()
        self.main_root.deiconify()
