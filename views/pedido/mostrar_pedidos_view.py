import tkinter as tk
from controllers.pedido_controller import PedidoController


class MostrarPedidosView:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.pedido_controller = PedidoController()
        self.root.title("Pedidos Registrados")
        self.root.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
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
        self.list_box_pedidos.delete(0, tk.END)

        pedidos = self.pedido_controller.listar_pedidos()

        pedidos_dict = {}  # Dicionário para armazenar todos os pedidos
        for pedido in pedidos:
            pedido_id = pedido[0]  # Obtendo o id do pedido
            data_pedido = pedido[1]  # E também a data

            # Se o ped_id ainda não estiver no dict, add uma nova entrada com a data do ped e uma list para os itens
            if pedido_id not in pedidos_dict:
                pedidos_dict[pedido_id] = {"data": data_pedido, "itens": []}
            pedidos_dict[pedido_id]["itens"].append(pedido[2:])  # Adicionando o cod_item e qtde a list do dict

        # Varrendo o dicionário do pedido
        for pedido_id, pedido_info in pedidos_dict.items():
            self.list_box_pedidos.insert(tk.END, f"Pedido ID: {pedido_id}, Data: {pedido_info['data']}")
            # Colocando todos os itens no listbox
            for item in pedido_info["itens"]:
                cod_item, quantidade = item
                self.list_box_pedidos.insert(tk.END, f"  Item ID: {cod_item}, Quantidade: {quantidade}")
            self.list_box_pedidos.insert(tk.END, "")  # Linha em branco para separar os pedidos

    def voltar(self):
        self.root.destroy()
        self.main_root.deiconify()
