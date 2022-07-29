import tkinter as tk
from tkinter import ttk, filedialog







# Config Window:
def configWindow_popup(root, route, routes_list, file_route, function_open):


    config_window = tk.Toplevel(root)

    config_window.config(bg = '#802727') # Config window.
    res = [500, 200]
    config_window.geometry(f'{res[0]}x{res[1]}')
    config_window.resizable(False, False)
    config_window.iconbitmap(r'.\Resources\Icons\DownTool.ico')
    config_window.title('Configurations')

    title = tk.Label(config_window, text = 'Configurations', font = ('Arial', 30, 'italic bold'), bg = '#802727', fg = '#f5f5f5')
    title.place(relx = .5, rely = .2, anchor = 'center')


    # Download button.
    style_button = ttk.Style()
    style_button.theme_use('alt')
    style_button.configure('TButton', background = '#cc6b6b', foreground = 'black', width = 20, focusthickness = 3, relief = 'flat', )
    style_button.map('TButton', background = [('active', '#cc6b6b')], relief = 'flat')





    def open_route():
        global route


        route_ask = filedialog.askdirectory(initialdir = 'C:/',
                            title = 'Selecciona una carpeta!')



        if route_ask == '':
            route = routes_list[-1]
            p_route_text.config(text = f'Predefined route: {route}')


        else:
            a = function_open()
            route = route_ask
            routes_list.append(route)

            a.seek(0)
            a.write(route)
            a.close()


            print(routes_list)

            p_route_text.config(text = f'Predefined route: {route}')


    change_route_button = ttk.Button(config_window, text = 'Change', command = open_route, width = 20, cursor = 'hand1')
    change_route_button.place(relx=.65, rely = .6, anchor = 'w')


    # Options:
        # predefined routed.
    p_route = route
    p_route_text = tk.Label(config_window, text = f'Predefined route: {p_route}', font = ('Arial', 10, 'italic'), bg = '#802727', fg = 'white')
    p_route_text.place(relx = .07, rely = .6, anchor = 'w')


