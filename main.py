from views.main_view import MainView
import tkinter as tk

if __name__ == "__main__":
    """
    Ponto de entrada principal da aplicação.

    Cria uma instância da classe MainView para iniciar a interface gráfica do sistema de pedidos.
    """
    root = tk.Tk()  # Cria a janela principal
    app = MainView(root)  # Inicializa a aplicação principal
    root.mainloop()  # Inicia o loop principal de eventos da interface gráfica
