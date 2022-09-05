import tkinter as tk
from tkinter import ttk, filedialog







# Config Window:
def aboutme_popup(root):


    config_window = tk.Toplevel(root)

    config_window.config(bg = '#FE5A56') # Config window.
    res = [500, 500]
    config_window.geometry(f'{res[0]}x{res[1]}')
    config_window.resizable(False, False)
    config_window.iconbitmap(r'.\Resources\Icons\DownTool_2.ico')
    config_window.title('About me')

    title = tk.Label(config_window, text = 'About Me', font = ('Arial', 30, 'italic bold'), bg = '#FE5A56', fg = '#f5f5f5')
    title.place(relx = .5, rely = .2, anchor = 'center')


    # Options:
        # predefined routed
    p_route_text = tk.Label(config_window, text = f'Actualización 1.4.5!\n- Metadata en todos los formatos!\n- Metada especial si descargas tus playlist de spotify!\n- Algunos bugs arreglados!\n- Ubicación de la miniatura temporal, movida.\n\n\n\n1.4.5 DownTool', font = ('Arial', 10, 'italic'), bg = '#FE5A56', fg = 'white')
    p_route_text.place(relx = .5, rely = .6, anchor = 'center')


