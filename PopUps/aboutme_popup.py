import tkinter as tk
from tkinter import ttk, filedialog







# Config Window:
def aboutme_popup(root):


    config_window = tk.Toplevel(root)

    config_window.config(bg = '#fe555c') # Config window.
    res = [500, 500]
    config_window.geometry(f'{res[0]}x{res[1]}')
    config_window.resizable(False, False)
    config_window.iconbitmap(r'.\Resources\Icons\DownTool_2.ico')
    config_window.title('About me')

    title = tk.Label(config_window, text = 'About Me', font = ('Arial', 30, 'italic bold'), bg = '#fe555c', fg = '#f5f5f5')
    title.place(relx = .5, rely = .2, anchor = 'center')


    # Options:
        # predefined routed
    p_route_text = tk.Label(config_window, text = f'Hola! La versión 1.2 aporta un nuevo diseño y se solucionó algunos problemas con las rutas predefinidas!\n\n\n\n1.2 DownTool', font = ('Arial', 10, 'italic'), bg = '#fe555c', fg = 'white')
    p_route_text.place(relx = .5, rely = .6, anchor = 'center')


