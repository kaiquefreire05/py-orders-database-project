import tkinter as tk
from tkinter import messagebox

from controllers.pedido_controller import PedidoController


class ExcluiPedidoView:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.root.title("Excluir pedido")
        self.root.geometry("400x400")
        self.pedido_controller = PedidoController()
        self.create_widgets()

    def create_widgets(self):
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        tk.Label(self.root, text="Digite o ID do pedido:").grid(row=2, column=0, padx=10, pady=5
                                                                , sticky='e')
        self.entry_id = tk.Entry(self.root)
        self.entry_id.grid(row=2, column=1, sticky='w', padx=10, pady=5)
        tk.Button(self.root, text="Excluir pedido", command=self.confirmar_exclusao).grid(row=3, column=1, padx=10
                                                                                          , columnspan=2, pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=4, column=0, columnspan=2)

    def confirmar_exclusao(self):
        pedido_id = self.entry_id.get()

        # Verificando se o campo foi preenchido
        if not pedido_id:
            messagebox.showerror("Erro", "Insira o ID do pedido")
            return

        resposta = messagebox.askyesno("Confirmação", f"Tem certeza que deseja remover o pedido com ID {pedido_id}?")
        if resposta:
            self.excluir_pedido(pedido_id)

    def excluir_pedido(self, pedido_id):
        try:
            # Transformando em inteiro
            pedido_id = int(pedido_id)
            # Tentando excluír e verificando o retorno
            sucesso = self.pedido_controller.excluir_pedido(pedido_id)
            if sucesso:
                messagebox.showinfo("Sucesso", "O pedido foi excluído com sucesso!")
            else:
                messagebox.showerror("Erro", f"Não existe pedido com o ID {pedido_id}")

        except ValueError:
            messagebox.showerror("Erro", "ID do pedido inválido.")

    def voltar(self):
        self.root.destroy()
        self.main_root.deiconify()
