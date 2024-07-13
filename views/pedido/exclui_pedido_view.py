import tkinter as tk
from tkinter import messagebox

from controllers.pedido_controller import PedidoController


class ExcluiPedidoView:
    """
        View para exclusão de um pedido existente.

        Attributes:
            root (tk.TK): Janela principal da aplicação.
            main_root (tk.TK): Referência à janela principal para retornar após fechar esta view.
            pedido_controller (PedidoController): Controlador de pedidos para interação com o modelo e banco de dados.
            entry_id (tk.Entry): Campo de entrada para o ID do pedido a ser excluído.
    """
    def __init__(self, root, main_root):
        """
            Inicializa a view de exclusão de pedido.

            Args:
                root (tk.TK): Janela principal da aplicação.
                main_root (tk.TK): Referência à janela principal para retornar após fechar esta view.
        """

        self.root = root
        self.main_root = main_root
        self.root.title("Excluir pedido")
        self.root.geometry("600x500")
        self.pedido_controller = PedidoController()
        self.create_widgets()

    def create_widgets(self):
        """
            Cria os widgets na janela de exclusão de pedido.
        """
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        tk.Label(self.root, text="Digite o ID do pedido:").grid(row=2, column=0, padx=10, pady=5
                                                                , sticky='e')
        self.entry_id = tk.Entry(self.root)
        self.entry_id.grid(row=2, column=1, sticky='w', padx=10, pady=5)
        tk.Button(self.root, text="Excluir pedido", command=self.confirmar_exclusao).grid(row=3, column=0, padx=10
                                                                                          , columnspan=2, pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=4, column=0, columnspan=2)

    def confirmar_exclusao(self):
        """
            Confirma a exclusão do pedido com base no ID fornecido pelo usuário.
        """
        pedido_id = self.entry_id.get()  # Obtendo o ID do pedido

        # Verificando se o campo foi preenchido
        if not pedido_id:
            messagebox.showerror("Erro", "Insira o ID do pedido")
            return

        # Condição de resposta
        resposta = messagebox.askyesno("Confirmação", f"Tem certeza que deseja remover o pedido com ID {pedido_id}?")
        if resposta:
            self.excluir_pedido(pedido_id)

    def excluir_pedido(self, pedido_id):
        """
            Tenta excluir o pedido com o ID fornecido.

            Args:
                pedido_id (str): ID do pedido a ser excluído.
        """
        try:
            # Transformando em inteiro
            pedido_id = int(pedido_id)
            # Tentando excluír e verificando o retorno
            sucesso = self.pedido_controller.excluir_pedido(pedido_id)

            # Se retornar True
            if sucesso:
                messagebox.showinfo("Sucesso", "O pedido foi excluído com sucesso!")
            else:  # Senão
                messagebox.showerror("Erro", f"Não existe pedido com o ID {pedido_id}")

        except ValueError:
            messagebox.showerror("Erro", "ID do pedido inválido.")

    def voltar(self):
        """
            Fecha a janela de exclusão de pedido e retorna à janela anterior.
        """
        self.root.destroy()
        self.main_root.deiconify()
