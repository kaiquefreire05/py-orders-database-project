import tkinter as tk
from controllers.pedido_controller import PedidoController
from tkinter import messagebox
from tkcalendar import DateEntry
from models.pedido import Pedido
from models.item_pedido import ItemPedido


class CadastroPedidoView:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.pedido_controller = PedidoController()
        self.root.title("Cadastro de Pedido")
        self.root.geometry("400x400")
        self.itens_pedido = list()
        self.create_widgets()

    def create_widgets(self):

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        tk.Label(self.root, text="Data do Pedido").grid(row=0, column=0, stick='e', padx=10, pady=5)
        self.entry_data_pedido = DateEntry(self.root, date_pattern='yyyy-mm-dd')
        self.entry_data_pedido.grid(row=0, column=1, stick='w', padx=10, pady=5)

        tk.Button(self.root, text="Adicionar item", command=self.adicionar_item_frame).grid(row=1, column=0
                                                                                            , columnspan=2, pady=5)

        # Adicionando um frame
        self.frame_itens = tk.Frame(self.root)
        self.frame_itens.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(self.root, text="Registrar Pedido", command=self.registrar_pedido).grid(row=3, column=0
                                                                                          , columnspan=2, pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=4, column=0, columnspan=2, pady=10)

    def adicionar_item_frame(self):
        row = len(self.itens_pedido)  # Qtde de linhas nos itens pedido

        entry_item_id = tk.Entry(self.frame_itens)
        entry_item_id.grid(row=row, column=0, padx=5, pady=5)
        self.set_placeholder(entry_item_id, "Item ID")

        entry_item_qtde = tk.Entry(self.frame_itens)
        entry_item_qtde.grid(row=row, column=1, padx=5, pady=5)
        self.set_placeholder(entry_item_qtde, "Quantidade")

        btn_remover = tk.Button(self.frame_itens, text="Remover item", command=lambda: self.remover_item_frame(row))
        btn_remover.grid(row=row, column=2, padx=5, pady=5)

        self.itens_pedido.append((entry_item_id, entry_item_qtde, btn_remover))  # Adicionando em uma tupla

    @staticmethod
    def set_placeholder(entry, placeholder):
        # Função para lidar com o evento de foco no campo de entrada
        def on_focus_in(event):
            # Verifica se o texto atual é igual ao placeholder
            if entry.get() == placeholder:
                # Se for igual, apaga o texto e muda a cor do texto para preto
                entry.delete(0, tk.END)
                entry.config(fg='black')

        # Função para lidar com o evento de perda de foco no campo de entrada
        def on_focus_out(event):
            # Verifica se o campo de entrada está vazio
            if entry.get() == '':
                # Se estiver vazio, insere o placeholder de volta e muda a cor do texto para cinza
                entry.insert(0, placeholder)
                entry.config(fg='grey')

        # Insere o placeholder inicialmente no campo de entrada e configura a cor do texto para cinza
        entry.insert(0, placeholder)
        entry.config(fg='grey')

        # Vincula os eventos de foco e perda de foco às funções definidas acima
        entry.bind('<FocusIn>', on_focus_in)
        entry.bind('<FocusOut>', on_focus_out)

    def remover_item_frame(self, row):
        for widget in self.itens_pedido[row]:
            widget.grid_forget()
        self.itens_pedido[row] = None  # Marcando a posição como None

    def registrar_pedido(self):
        # Obtém os valores dos campos de entrada
        data_pedido = self.entry_data_pedido.get()
        pedido = Pedido(data_pedido)

        itens_pedido = []  # Lista para armazenar os itens do pedido
        # Iterando sobre cada posição da tupla
        for item_widgets in self.itens_pedido:
            if item_widgets:
                item_id, qtde_item, _ = item_widgets
                try:
                    item_id = int(item_id.get())  # Obtendo ID
                    qtde_item = int(qtde_item.get())  # Obtendo quantidade do produto
                    item_pedido = ItemPedido(item_id, qtde_item, data_pedido)  # Criando objeto ItemPedido
                    itens_pedido.append(item_pedido)  # Adicionado na lista de itens de pedido

                except ValueError:
                    messagebox.showerror("Erro", "IDs e quantidade precisam ser inteiros")
                    return

        # Verificando se foi adicionado itens no pedido
        if not itens_pedido:
            messagebox.showerror("Erro", "Adicione pelo menos um item no pedido")
            return

        # Tentando registrar o pedido
        try:
            self.pedido_controller.registrar_pedido(pedido, itens_pedido)
            messagebox.showinfo("Sucesso", "Pedido foi registrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao registrar o pedido {str(e)}")

    def voltar(self):
        self.root.destroy()  # Fecha a janela de registro de pedido
        self.main_root.deiconify()  # Reexibe a janela principal
