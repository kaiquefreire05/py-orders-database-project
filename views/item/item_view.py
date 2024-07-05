import tkinter as tk
from controllers.item_controller import ItemController
from views.item.item_cadastro_view import CadastroItemView
from views.item.mostrar_itens_view import MostrarItens
from views.item.atualizar_item_view import AtualizarItemView
from views.item.excluir_item_view import ExcluirItemView


class ItemView:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.root.title("Opções item")  # Define o título da janela de registro de item
        self.root.geometry("400x400")  # Define o tamanho da janela de registro de item

        self.item_controller = ItemController()  # Inicializa o controlador de itens
        self.create_widgets()  # Cria os widgets na janela

    def create_widgets(self):
        tk.Button(self.root, text="Registrar item", command=self.open_cadastro_window).pack(pady=10)
        tk.Button(self.root, text="Mostrar todos itens", command=self.open_mostra_itens).pack(pady=10)
        tk.Button(self.root, text="Atualizar item", command=self.open_atualizar_item).pack(pady=10)
        tk.Button(self.root, text="Excluir item", command=self.open_excluir_item).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).pack(pady=10)

    def voltar(self):
        self.root.destroy()  # Fecha a janela de registro de item
        self.main_root.deiconify()  # Reexibe a janela principal

    def open_cadastro_window(self):
        self.root.withdraw()  # Oculta a janela principal
        item_window = tk.Toplevel(self.root)  # Cria uma nova janela de nível superior
        # Inicializa a visão de item com a nova janela e a referência da janela principal
        CadastroItemView(item_window, self.root)

    def open_mostra_itens(self):
        self.root.withdraw()
        item_window = tk.Toplevel(self.root)
        MostrarItens(item_window, self.root)

    def open_atualizar_item(self):
        self.root.withdraw()
        item_window = tk.Toplevel(self.root)
        AtualizarItemView(item_window, self.root)

    def open_excluir_item(self):
        self.root.withdraw()
        item_window = tk.Toplevel(self.root)
        ExcluirItemView(item_window, self.root)


