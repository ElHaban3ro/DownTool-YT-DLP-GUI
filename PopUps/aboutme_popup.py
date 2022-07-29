import tkinter as tk
from tkinter import ttk, filedialog







# Config Window:
def aboutme_popup(root):


    config_window = tk.Toplevel(root)

    config_window.config(bg = '#802727') # Config window.
    res = [500, 500]
    config_window.geometry(f'{res[0]}x{res[1]}')
    config_window.resizable(False, False)
    config_window.iconbitmap(r'.\Resources\Icons\DownTool.ico')
    config_window.title('About me')

    title = tk.Label(config_window, text = 'About Me', font = ('Arial', 30, 'italic bold'), bg = '#802727', fg = '#f5f5f5')
    title.place(relx = .5, rely = .2, anchor = 'center')


    # Options:
        # predefined routed
    p_route_text = tk.Label(config_window, text = f'Gracias por descargar esta versión de\nDownTool, todo el código fuente está en mi github: ElHaban3ro.\nIré actualizando cuando deba, pero la app es funcional.\nLa app no tiene no tiene incorporado el elegir la\ncalidad porque realmente no es lo que necesito,\npero en alguna parte de los modulos hay un bucle que accede\n a las calidades :)\n\n\n\n1.1 DownTool', font = ('Arial', 10, 'italic'), bg = '#802727', fg = 'white')
    p_route_text.place(relx = .5, rely = .6, anchor = 'center')


