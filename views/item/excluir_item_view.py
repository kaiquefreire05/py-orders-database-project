import tkinter as tk
from controllers.item_controller import ItemController
from tkinter import messagebox


class ExcluirItemView:
    """
        Classe para criar uma interface gráfica para excluir itens.

        Attributes:
            root (tk.TK): A janela principal para a visualização de exclusão de item.
            main_root (tk.TK): Referência à janela principal da aplicação.
            item_controller (ItemController): O controlador para gerenciar dados de item.
    """
    def __init__(self, root, main_root):
        """
            Inicializa a instância ExcluirItemView.

            Args:
                root (tk.TK): A janela principal para a visualização de exclusão de item.
                main_root (tk.TK): Referência à janela principal da aplicação.
        """
        self.root = root
        self.main_root = main_root
        self.root.title("Excluir item")
        self.root.geometry("600x500")
        self.item_controller = ItemController()  # Controlador do  BD de itens
        self.create_widgets()

    def create_widgets(self):
        """
            Cria os widgets para a visualização de exclusão de item.

            Este método configura o layout em grid e cria rótulos, campos de entrada e botões para interação do usuário.
        """

        # Configurando as colunas
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        tk.Label(self.root, text="Digite o ID do pedido para ser excluído:").grid(row=2, column=0, sticky='e'
                                                                                  , padx=10, pady=5)
        self.entry_id = tk.Entry(self.root)
        self.entry_id.grid(row=2, column=1, sticky='w', padx=10, pady=5)

        # Botão
        tk.Button(self.root, text="Excluir item", command=self.confirmar_exclusao).grid(row=5, column=0
                                                                                        , columnspan=2, pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=6, column=0, columnspan=2)

    def confirmar_exclusao(self):
        """
            Confirma a exclusão do item com base no ID inserido pelo usuário.

            Verifica se um ID válido foi inserido. Em caso positivo, exibe uma mensagem de confirmação.
            Em caso negativo, exibe um erro. Após confirmação, chama o método (excluir_item) para realizar a exclusão.
        """
        item_id = self.entry_id.get()  # Obtendo ID do item

        # Verificando se alguma coisa foi inserida
        if not item_id:
            messagebox.showerror("Erro", "Informe o ID do item")
            return

        # Verificando a resposta
        resposta = messagebox.askyesno("Confirmação", f"Tem certeza que deseja remover o item com o ID {item_id}?")
        if resposta:
            self.excluir_item(item_id)

    def excluir_item(self, item_id):
        """
            Tenta excluir um item com base no ID fornecido.

            Args:
                item_id (str): O ID do item a ser excluído.

            Exibe uma mensagem de sucesso se o item for excluído com sucesso.
            Se o ID do item for inválido ou se o item não existir, exibe uma mensagem de erro correspondente.
        """

        # Tentando excluír o item
        try:
            # Converte o item_id para inteiro
            item_id = int(item_id)
            # Tenta excluir o item e verifica o retorno
            sucesso = self.item_controller.excluir_item(item_id)

            # Verificando se teve sucesso
            if sucesso:
                messagebox.showinfo("Sucesso", "O item foi excluído com sucesso.")
            # Senão o item não existe
            else:
                messagebox.showerror("Erro", f"Não existe item com o ID {item_id}.")
        # Lançando erro
        except ValueError:
            messagebox.showerror("Erro", "ID do item inválido.")

    def voltar(self):
        """
            Retorna à janela anterior da aplicação.

            Este método fecha a janela atual e torna visível novamente a janela principal da aplicação.
        """
        self.root.destroy()
        self.main_root.deiconify()
