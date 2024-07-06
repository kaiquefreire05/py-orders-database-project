import tkinter as tk
from controllers.item_controller import ItemController


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

        tk.Label(self.root, text="Digite o ID do pedido para ser excluído:").grid(row=0, column=0, sticky='e'
                                                                                  , padx=10, pady=5)
        self.entry_id = tk.Entry(self.root)
        self.entry_id.grid(row=0, column=1, sticky='w', padx=10, pady=5)

        # Botão
        tk.Button(self.root, text="Excluir item", command=self.confirmar_exclusao).grid(row=5, column=0
                                                                                        , columnspan=2, pady=10)
        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=6, column=0, columnspan=2)

    def confirmar_exclusao(self):
        return

    def excluir_item(self):
        return

    def voltar(self):
        self.root.destroy()
        self.main_root.deiconify()
