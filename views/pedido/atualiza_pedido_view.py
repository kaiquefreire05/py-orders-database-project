import tkinter as tk
from controllers.pedido_controller import PedidoController
from tkinter import messagebox
from tkcalendar import DateEntry
from models.item_pedido import ItemPedido
from models.pedido import Pedido


class AtualizaPedidoView:
    """
    View para atualizar um pedido existente.

    Attributes:
        root (tk.TK): Janela principal da aplicação.
        main_root (tk.TK): Referência à janela principal para retornar após fechar esta view.
        pedido_controller (PedidoController): Controlador de pedidos para interação com o modelo e banco de dados.
        itens_pedido (list): Lista de widgets para os itens do pedido.
        frame_dados_pedidos (tk.Frame): Frame para exibir os dados do pedido.
        frame_itens (tk.Frame): Frame para exibir os itens do pedido.
        entry_id (tk.Entry): Campo de entrada para o ID do pedido.
        entry_data_pedido (DateEntry): Campo de entrada para a data do pedido.
    """
    def __init__(self, root, main_root):
        """
            Inicializa a view de atualização de pedido.

            Args:
                root (tk.TK): Janela principal da aplicação.
                main_root (tk.TK): Referência à janela principal para retornar após fechar esta view.
        """
        self.root = root
        self.main_root = main_root
        self.root.title("Atualizar pedido")
        self.root.geometry("600x500")
        self.pedido_controller = PedidoController()  # Controller de pedidos
        self.itens_pedido = list()  # Lista que vai armazenar os itens que serão registrados
        self.create_widgets()

    def create_widgets(self):
        """
            Cria os widgets na janela de atualização de pedido.
        """

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # ID do pedido
        tk.Label(self.root, text="Digite o ID do Pedido").grid(row=0, column=0, sticky='e', padx=10, pady=5)
        self.entry_id = tk.Entry(self.root)
        self.entry_id.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        tk.Button(self.root, text="Carregar Pedido", command=self.carregar_pedido).grid(pady=10, columnspan=2)

        # Frame para mostrar os dados do pedido
        self.frame_dados_pedidos = tk.Frame(self.root)
        self.frame_dados_pedidos.grid(row=1, column=0, columnspan=3, pady=10)

        tk.Label(self.frame_dados_pedidos, text="Data do Pedido:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.entry_data_pedido = DateEntry(self.frame_dados_pedidos, date_pattern='yyyy-mm-dd')
        self.entry_data_pedido.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        # Itens do Pedido
        tk.Label(self.frame_dados_pedidos, text="Itens do Pedido").grid(row=1, column=0, columnspan=2, pady=10)
        self.frame_itens = tk.Frame(self.frame_dados_pedidos)
        self.frame_itens.grid(row=2, column=0, columnspan=2, pady=10)

        # Botões
        tk.Button(self.root, text="Atualizar Pedido", command=self.atualizar_pedido).grid(row=2, column=0, columnspan=2
                                                                                          , pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=3, column=0, pady=10, columnspan=2)

        # Escondendo inicialmente os campos Data e Itens
        self.hide_dados_pedidos()

    def carregar_pedido(self):
        """
            Carrega os detalhes de um pedido existente com base no ID fornecido.
        """

        try:
            id = int(self.entry_id.get())  # ID de parâmetro
            pedido, itens = self.pedido_controller.carrega_pedido(id)  # Carregando o pedido, com os itens

            # Verificando se o pedido não existe
            if pedido is None:
                messagebox.showerror("Erro", "Esse pedido não existe")
                return

            # Mostrando os campos ocultos
            self.show_dados_pedidos()
            # Preenchendo a data do pedido
            self.entry_data_pedido.set_date(pedido.data_pedido)

            # Limpando os widgets dos itens
            for w in self.frame_itens.winfo_children():
                w.destroy()

            # Preenchendo os widgets com os itens
            for i, (item_id, qtde) in enumerate(itens):
                entry_item_id = tk.Entry(self.frame_itens)
                entry_item_id.grid(row=i, column=0, padx=5, pady=5)
                entry_item_id.insert(0, str(item_id))

                entry_qtde = tk.Entry(self.frame_itens)
                entry_qtde.grid(row=i, column=1, padx=5, pady=5)
                entry_qtde.insert(0, str(qtde))

                btn_remover = tk.Button(self.frame_itens, text="Remover Item",
                                        command=lambda idx=i: self.remover_item_frame(idx))
                btn_remover.grid(row=i, column=2, padx=5, pady=5)

                # Adicionando os campos na lista
                self.itens_pedido.append((entry_item_id, entry_qtde, btn_remover))

            # Botão para adicionar novo item
            (tk.Button(self.frame_dados_pedidos, text="Adicionar Item", command=self.adicionar_item_frame)
             .grid(row=3, column=0, columnspan=2, pady=10))

        except ValueError:
            messagebox.showerror("Erro", "ID inválido")

    def atualizar_pedido(self):
        """
            Atualiza o pedido com base nos dados fornecidos.
        """

        # Obtendo os valores do campo
        pedido_id = int(self.entry_id.get())
        data_pedido = self.entry_data_pedido.get()
        itens = list()  # Lista para armazenar os itens atualizados

        for item_widget in self.itens_pedido:
            if item_widget:
                item_id, qtde_item, _ = item_widget
                try:
                    item_id = int(item_id.get())
                    qtde_item = int(qtde_item.get())
                    item_pedido = ItemPedido(item_id=item_id, quantidade=qtde_item, data_pedido=data_pedido)
                    itens.append(item_pedido)
                except ValueError:
                    messagebox.showerror("Erro", "ID e quantidade precisam ser inteiros")
                    return
        # Tentando atualizar o pedido
        try:
            pedido = Pedido(data_pedido=data_pedido)
            self.pedido_controller.atualizar_pedido(pedido_id, pedido, itens)
            messagebox.showinfo("Sucesso", "Pedido atualizado com sucesso")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar o pedido. Erro: {str(e)}")

    def show_dados_pedidos(self):
        """
            Mostra os campos de dados do pedido na interface.
        """
        self.frame_dados_pedidos.grid(row=1, column=0, columnspan=3, pady=10)

    def hide_dados_pedidos(self):
        """
            Esconde os campos de dados do pedido na interface.
        """
        self.frame_dados_pedidos.grid_forget()

    def adicionar_item_frame(self):
        """
            Adiciona um novo campo para inserção de item na interface.
        """
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

    def remover_item_frame(self, row):
        """
            Remove um campo de item da interface.

            Args:
                row (int): Índice da linha do item a ser removido.
        """

        for widget in self.itens_pedido[row]:
            widget.grid_forget()
        self.itens_pedido[row] = None

    @staticmethod
    def set_placeholder(entry, placeholder):
        """
            Configura um placeholder para um campo de entrada.

            Args:
                entry (tk.Entry): Campo de entrada para configurar o placeholder.
                placeholder (str): Texto do placeholder.
        """
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

    def voltar(self):
        """
            Fecha a janela de atualização de pedido e retorna à janela anterior.
        """
        self.root.destroy()
        self.main_root.deiconify()
