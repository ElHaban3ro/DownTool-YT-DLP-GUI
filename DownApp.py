# Libreries.
import tkinter as tk
from tkinter import Checkbutton, IntVar, ttk
from threading import Thread

from tkinter import filedialog
import tkinter.font as tkf

from PIL import Image, ImageTk



# My Modules.
from Modules.download_audio import audio_downloader
from Modules.download_video import video_downloader

from PopUps.configuration_popup import configWindow_popup
from PopUps.aboutme_popup import aboutme_popup




# Config main window.
root = tk.Tk() # Create "Window".
root.config(bg = '#260b12') # Config window.
res = [700, 415]
root.geometry(f'{res[0]}x{res[1]}')
root.resizable(False, False)


root.title('DownTool')
root.iconbitmap(r'.\Resources\Icons\DownTool.ico')







# Download button.
style_button = ttk.Style()
style_button.theme_use('alt')
style_button.configure('TButton', background = '#cc6b6b', foreground = 'black', width = 20, focusthickness = 3, relief = 'flat', )
style_button.map('TButton', background = [('active', '#cc6b6b')], relief = 'flat')



# Download button.
style_button = ttk.Style()
style_button.theme_use('alt')
style_button.configure('TEntry', background = '#4b2c2c', foreground = 'black', width = 20, focusthickness = 3, relief = 'flat',  fieldbackground = '#e4e4e4', padding = 5)
style_button.map('TEntry', background = [('active', '#e4e4e4')], relief = 'flat')




# Download button.
style_button = ttk.Style()
style_button.theme_use('alt')
style_button.configure('TCheckbutton', background = '#802727', foreground = 'black', width = 20, focusthickness = 3, relief = 'flat',  fieldbackground = '#e4e4e4', padding = 5)
style_button.map('TCheckbutton', background = [('active', '#e4e4e4')], relief = 'flat')



# Downloads history.
downloads_history = []






video_info_frame = tk.Frame(root, bg = '#aa3333', width = 670, height = 200)
video_info_frame.place(relx = .5, rely = .28, anchor = 'center')

video_miniature = tk.Frame(video_info_frame, bg = '#260b12', width = 320, height = 180)
video_miniature.place(relx = .255, rely = .5, anchor = tk.CENTER)



w = res[0]
h = res[1]





form_download = tk.Frame(root, bg = '#aa3333', width = 670, height = 165)
form_download.place(relx = .5, rely = .76, anchor= tk.CENTER)

download_config_layer = tk.Frame(form_download, bg = '#802727', width = 300, height = 147)
download_config_layer.place(relx = .24, rely = .5, anchor = 'center')


history_layer = tk.Frame(form_download, bg = '#802727', width = 334, height = 147)
history_layer.place(relx = .983, rely = .5, anchor = 'e')


history_title = tk.Label(history_layer, text = 'History', font = ('Arial', 20, 'bold italic'), bg = '#802727', fg = '#f5f5f5')
history_title.place(relx = .5, rely = .15, anchor = 'center')



history_text = tk.Label(history_layer, text = '', font = ('Arial', 10, 'italic'), bg = '#802727', fg = 'yellow', width=300)
history_text.place(relx = .5, rely = .35, anchor = 'n')






# Create input text.
input_link = ttk.Entry(download_config_layer, width = 45, style = 'TEntry')
input_link.place(relx = .5, rely = .15, anchor = tk.CENTER)




# Route select.

route = 'C:/'
route_open = ''

def open_file():
    global route
    global route_open
    route_open = open(r'.\Resources\Config\route.txt', 'r+')
    route = route_open.readline()

    return route_open


open_file()

routes = [route]





features_text_title = tk.Label(video_info_frame, text = 'Unknown Video', font = ('Arial', 20, 'bold italic'), bg = '#aa3333', fg = '#f5f5f5')
features_text_title.place(relx = .52, rely = .16, anchor = 'w')


features_text_channel = tk.Label(video_info_frame, text = 'Channel: Unknown', font = ('Arial', 10, 'italic'), bg = '#aa3333', fg = '#f5f5f5')
features_text_channel.place(relx = .52, rely = .3, anchor = 'w')

features_text_more = tk.Label(video_info_frame, text = 'Weight and format: 0MB - ###', font = ('Arial', 10, 'italic'), bg = '#aa3333', fg = '#f5f5f5')
features_text_more.place(relx = .52, rely = .4, anchor = 'w')


# Route text.
route_text = tk.Label(video_info_frame, text = f'Save route: {route}', font = ('Arial', 10, 'italic'), bg = '#aa3333', fg ='#f5f5f5')
route_text.place(relx = .52, rely = .5, anchor = 'w')

restant_text = tk.Label(video_info_frame, text = f'Approximate time: 00:00', font = ('Arial', 10, 'italic'), bg = '#aa3333', fg = '#f5f5f5')
restant_text.place(relx = .52, rely = .6, anchor = 'w')

percent_text = tk.Label(video_info_frame, text = f'', font = ('Arial', 15, 'italic bold'), bg = '#aa3333', fg = '#f5f5f5')
percent_text.place(relx = .52, rely = .9, anchor = 'w')





# Checkbox zone.
    # Title format.
format_title = tk.Label(download_config_layer, text = 'Select a format:', font = ('Arial', 15, 'italic bold'), bg = '#802727', fg = '#f5f5f5')
format_title.place(relx = .03, rely = .61, anchor = 'w')


MP3 = IntVar()
mp3_option = Checkbutton(download_config_layer, text = 'MP3', variable = MP3, onvalue = 1, offvalue = 0)
mp3_option.configure(bg = '#802727', activebackground = '#802727')
mp3_option.place(relx = .12, rely = .8, anchor = 'w')


MP4 = IntVar()
mp4_option = Checkbutton(download_config_layer, text = 'MP4', variable = MP4, onvalue = 1, offvalue = 0)
mp4_option.configure(bg = '#802727', activebackground = '#802727')
mp4_option.place(relx = .4, rely = .8, anchor = 'w')


def open_route():
    global route
    route_ask = filedialog.askdirectory(initialdir = 'C:/',
                                  title = 'Selecciona una carpeta!')



    if route_ask == '':
        route = routes[-1]
        route_text.config(text = f'Save route: {route}')


    else:
        route = route_ask
        routes.append(route)
        print(routes)

        route_text.config(text = f'Save route: {route}')








# Open browser button.
folder_icon = './Resources/Icons/folder.png'
folder_icon = ImageTk.PhotoImage(Image.open(folder_icon).resize((15, 15)))

browser_button = ttk.Button(download_config_layer, text = 'Folder', width = 15, command = open_route, cursor = 'plus', image = folder_icon)
browser_button.place(relx=.52, rely = .4, anchor = 'w')




# Download function  anti bug.
def download_function(): # Create new thread (bug)

    if MP3.get() == 1 and MP4.get() != 1:

        if input_link.get() == '':
            tk.messagebox.showwarning('Warning!', 'Specify the download link.')


        elif route == 'C:/':
            tk.messagebox.showerror('¡Error!', 'Make sure to choose a path other than C:/\n(This causes permission errors)')

        else:
            # audio_downloader(link_video = input_link.get(), button = download_button)
            a = Thread(target = lambda: audio_downloader(link_video = input_link.get(), button = download_button, inputContent= input_link, route = route, route_miniature = route, folder_button = browser_button, frame = video_miniature, title_widget = features_text_title, channel = features_text_channel, percent_text = percent_text, restant_widget = restant_text, bytes_widget = features_text_more, checkbox_mp3 = mp3_option, checkbox_mp4 = mp4_option, list_history = downloads_history, h_text = history_text)).start()




    elif MP4.get() == 1 and MP3.get() != 1:

        if input_link.get() == '':
            tk.messagebox.showwarning('Warning!', 'Specify the download link.')


        elif route == 'C:/':
            tk.messagebox.showerror('¡Error!', 'Make sure to choose a path other than C:/\n(This causes permission errors)')

        else:
            a = Thread(target = lambda: video_downloader(link_video = input_link.get(), button = download_button, inputContent= input_link, route = route, route_miniature = route, folder_button = browser_button, frame = video_miniature, title_widget = features_text_title, channel = features_text_channel, percent_text = percent_text, restant_widget = restant_text, bytes_widget = features_text_more, checkbox_mp3 = mp3_option, checkbox_mp4 = mp4_option, list_history = downloads_history, h_text = history_text)).start()










    elif MP3.get() == 1 and MP4.get() == 1:
        tk.messagebox.showerror('Error Box!', 'Remember that you can only choose one format')

    else:
        tk.messagebox.showwarning('Warning!', 'Choose a format in which to download your content')



download_button = ttk.Button(download_config_layer, text = 'Download', command = download_function, width = 20, cursor = 'hand1')
download_button.place(relx=.03, rely = .4, anchor = 'w')





# Menu.
menu_bar = tk.Menu(root)
root.configure(menu = menu_bar)

def config_pop():
    open_file()
    configWindow_popup(root, route, routes, route_open, open_file)



configMenu = tk.Menu(menu_bar, tearoff = 0)
configMenu.add_command(label = 'Configure App', command = config_pop)




def aboutme_pop():
    aboutme_popup(root)



moreMenu = tk.Menu(menu_bar, tearoff = 0)
moreMenu.add_command(label = 'About Me', command = aboutme_pop)




menu_bar.add_cascade(label = 'Edit', menu = configMenu)
menu_bar.add_cascade(label = 'More', menu = moreMenu)




root.mainloop()