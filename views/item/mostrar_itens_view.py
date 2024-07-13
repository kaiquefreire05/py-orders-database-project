import tkinter as tk
from controllers.item_controller import ItemController


class MostrarItens:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.root.title("Mostrar itens cadastrados")
        self.root.geometry("600x500")
        self.item_controller = ItemController()  # Controlador de itens
        self.create_widgets()

    def create_widgets(self):

        # Configurar as colunas para garantir centralização
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        tk.Label(self.root, text="Clique no botão para listar todos os itens").grid(row=0, column=0, columnspan=3,
                                                                                    pady=10)
        tk.Button(self.root, text="Mostrar itens cadastrados", command=self.mostrar_itens).grid(row=1, column=1,
                                                                                                pady=10)

        # Adiciona um Listbox para mostrar os itens
        self.listbox_itens = tk.Listbox(self.root, width=60, height=10)
        self.listbox_itens.grid(row=3, column=0, columnspan=3, pady=10)

        tk.Button(self.root, text="Voltar", command=self.voltar).grid(row=5, column=1, pady=10)

    def mostrar_itens(self):
        # Limpando a listbox
        self.listbox_itens.delete(0, tk.END)

        itens = self.item_controller.listar_todos()  # Obtendo todos os itens
        if not itens:  # Se não existir itens
            self.listbox_itens.insert(tk.END, "Não tem nenhum item registrado.")
        else:
            # Mostrando todos os itens na list box
            for item in itens:
                self.listbox_itens.insert(tk.END, f'ID: {item[0]}, Nome: {item[1]}, Descrição: {item[2]}'
                                                  f', Preço: {item[3]}, Quantidade: {item[4]}')

    def voltar(self):
        self.root.destroy()
        self.main_root.deiconify()
