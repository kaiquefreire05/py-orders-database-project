import tkinter as tk
from controllers.item_controller import ItemController
from tkinter import messagebox


class ExcluirItemView:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.root.title("Excluir item")
        self.root.geometry("400x400")
        self.item_controller = ItemController()
        self.create_widgets()

    def create_widgets(self):
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
        item_id = self.entry_id.get()

        # Verificando se alguma coisa foi inserida
        if not item_id:
            messagebox.showerror("Erro", "Informe o ID do item")
            return

        # Verificando a resposta
        resposta = messagebox.askyesno("Confirmação", f"Tem certeza que deseja remover o item com o ID {item_id}?")
        if resposta:
            self.excluir_item(item_id)

    def excluir_item(self, item_id):
        try:
            # Converte o item_id para inteiro
            item_id = int(item_id)
            # Tenta excluir o item e verifica o retorno
            sucesso = self.item_controller.excluir_item(item_id)
            if sucesso:
                messagebox.showinfo("Sucesso", "O item foi excluído com sucesso.")
            else:
                messagebox.showerror("Erro", f"Não existe item com o ID {item_id}.")
        except ValueError:
            messagebox.showerror("Erro", "ID do item inválido.")

    def voltar(self):
        self.root.destroy()
        self.main_root.deiconify()
