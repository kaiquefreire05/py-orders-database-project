import tkinter as tk
from controllers.item_controller import ItemController
from views.item.item_cadastro_view import CadastroItemView
from views.item.mostrar_itens_view import MostrarItens
from views.item.atualizar_item_view import AtualizarItemView
from views.item.excluir_item_view import ExcluirItemView


class ItemView:
    """
        Classe para criar uma interface gráfica principal para gerenciar itens.

        Attributes:
            root (tk.TK): A janela principal da aplicação.
            main_root (tk.TK): A referência à janela principal da aplicação.
            item_controller (ItemController): O controlador para gerenciar operações de itens.
    """
    def __init__(self, root, main_root):
        """
            Inicializa a interface gráfica principal para gerenciar itens.

            Args:
                root (tk.TK): A janela principal da aplicação.
                main_root (tk.TK): A referência à janela principal da aplicação.
        """
        self.root = root
        self.main_root = main_root
        self.root.title("Opções item")  # Define o título da janela de registro de item
        self.root.geometry("600x500")  # Define o tamanho da janela de registro de item

        self.item_controller = ItemController()  # Inicializa o controlador de itens
        self.create_widgets()  # Cria os widgets na janela

    def create_widgets(self):
        """
            Cria os widgets (botões) na janela principal.

            Este método cria botões para as diferentes funcionalidades de gerenciamento de itens:
            - Cadastrar item
            - Mostrar todos os itens
            - Atualizar item
            - Excluir item
            - Voltar para a janela principal
        """
        # Criando os botões de redirecionamento
        tk.Button(self.root, text="Registrar item", command=self.open_cadastro_window).pack(pady=10)
        tk.Button(self.root, text="Mostrar todos itens", command=self.open_mostra_itens).pack(pady=10)
        tk.Button(self.root, text="Atualizar item", command=self.open_atualizar_item).pack(pady=10)
        tk.Button(self.root, text="Excluir item", command=self.open_excluir_item).pack(pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).pack(pady=10)

    def voltar(self):
        """
            Retorna à janela principal da aplicação.

            Este método fecha a janela atual de gerenciamento de itens e torna visível novamente a janela principal.
        """
        self.root.destroy()  # Fecha a janela de registro de item
        self.main_root.deiconify()  # Reexibe a janela principal

    def open_cadastro_window(self):
        """
            Abre uma nova janela para cadastrar um novo item.

            Este método oculta a janela principal, cria uma nova janela de nível superior para o cadastro de item
            e inicializa a classe (CadastroItemView) para gerenciar o cadastro.
        """
        self.root.withdraw()  # Oculta a janela principal
        item_window = tk.Toplevel(self.root)  # Cria uma nova janela de nível superior
        # Inicializa a visão de item com a nova janela e a referência da janela principal
        CadastroItemView(item_window, self.root)

    def open_mostra_itens(self):
        """
            Abre uma nova janela para mostrar todos os itens cadastrados.

            Este método oculta a janela principal, cria uma nova janela de nível superior para mostrar os itens
            e inicializa a classe (MostrarItens) para exibir os itens.
        """
        self.root.withdraw()  # Oculta a janela principal
        item_window = tk.Toplevel(self.root)  # Cria uma nova janela de nível superior
        # Inicializa a visão de item com a nova janela e a referência da janela principal
        MostrarItens(item_window, self.root)

    def open_atualizar_item(self):
        """
            Abre uma nova janela para atualizar um item existente.

            Este método oculta a janela principal, cria uma nova janela de nível superior para atualizar um item
            e inicializa a classe (AtualizarItemView) para gerenciar a atualização do item.
        """
        self.root.withdraw()  # Oculta a janela principal
        item_window = tk.Toplevel(self.root)  # Cria uma nova janela de nível superior
        # Inicializa a visão de item com a nova janela e a referência da janela principal
        AtualizarItemView(item_window, self.root)

    def open_excluir_item(self):
        """
            Abre uma nova janela para excluir um item existente.

            Este método oculta a janela principal, cria uma nova janela de nível superior para excluir um item
            e inicializa a classe (ExcluirItemView) para gerenciar a exclusão do item.
        """
        self.root.withdraw()  # Oculta a janela principal
        item_window = tk.Toplevel(self.root)  # Cria uma nova janela de nível superior
        # Inicializa a visão de item com a nova janela e a referência da janela principal
        ExcluirItemView(item_window, self.root)


