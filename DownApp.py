# Libreries.
from email.mime import image
import tkinter as tk
from tkinter import Checkbutton, IntVar, ttk, Radiobutton
from threading import Thread

from tkinter import filedialog, PhotoImage, Canvas
import tkinter.font as tkf

from PIL import Image, ImageTk



# My Modules.
from Modules.download_audio import audio_downloader
from Modules.download_video import video_downloader

from PopUps.configuration_popup import configWindow_popup
from PopUps.aboutme_popup import aboutme_popup

from Modules.download_spotify import audio_downloader_spotify

# Config main window.
root = tk.Tk() # Create "Window".



res = [700, 415]
root.geometry(f'{res[0]}x{res[1]}')
root.resizable(False, False)


root.title('DownTool')
root.iconbitmap(r'.\Resources\Icons\DownTool_2.ico')





fondo = tk.Label(root, text = '', font = ('Arial', 20, 'bold italic'), bg = '#FE5A56', fg = '#f5f5f5')
fondo.place(relx = .5, rely = .5, anchor = 'center', width=700, height=415
)



# Download button.
style_button = ttk.Style()
style_button.theme_use('alt')
style_button.configure('TButton', background = '#ffffff', foreground = 'black', width = 20, focusthickness = 3, relief = 'flat', )
style_button.map('TButton', background = [('active', '#e5e5e5')], relief = 'flat')



# Download input.
style_Entry = ttk.Style()
style_Entry.theme_use('alt')
style_Entry.configure('TEntry', background = '#4b2c2c', foreground = 'black', width = 20, focusthickness = 3, relief = 'flat',  fieldbackground = '#e4e4e4', padding = 5, borderwidth = 0, highlightthickness = 0)
style_Entry.map('TEntry', background = [('active', '#e4e4e4')], relief = 'flat')




# Download select options.
style_Check = ttk.Style()
style_Check.theme_use('alt')
style_Check.configure('TCheckbutton', background = '#802727', foreground = 'black', width = 20, focusthickness = 3, relief = 'flat',  fieldbackground = '#e4e4e4', padding = 5)
style_Check.map('TCheckbutton', background = [('active', '#e4e4e4')], relief = 'flat')



# Downloads history.
downloads_history = []





# Video Frame
video_info_frame = tk.Canvas(root, width = 670, bg = '#FE5A56', height = 200, borderwidth = 0, highlightthickness = 0)
video_info_frame.place(relx = .5, rely = .28, anchor = 'center')

video_miniature_frame = tk.Frame(video_info_frame, bg = '#ffffff', width = 320, height = 180)
video_miniature_frame.place(relx = .255, rely = .5, anchor = tk.CENTER)

video_miniature = tk.Frame(video_miniature_frame, bg = '#0b0024', width = 288, height = 155)
video_miniature.place(relx = .5, rely = .5, anchor = tk.CENTER)



w = res[0]
h = res[1]





form_download = tk.Frame(root, bg = '#FE5A56', width = 670, height = 165)
form_download.place(relx = .5, rely = .76, anchor= tk.CENTER)

download_config_layer = tk.Frame(form_download, bg = '#FE5A56', width = 300, height = 150, highlightthickness=5)
download_config_layer.config(highlightbackground = 'white', highlightcolor = 'white')

download_config_layer.place(relx = .24, rely = .5, anchor = 'center')


history_layer = tk.Frame(form_download, bg = '#FE5A56', width = 334, height = 150, highlightthickness=5)
history_layer.place(relx = .983, rely = .5, anchor = 'e')
history_layer.config(highlightbackground = 'white', highlightcolor = 'white')

# history_layer.place(relx = .24, rely = .5, anchor = 'center')


history_title = tk.Label(history_layer, text = 'History', font = ('Arial', 15, 'bold italic'), bg = '#FE5A56', fg = '#f5f5f5', bd=-2, borderwidth=0)
history_title.place(relx = .15, rely = .15, anchor = 'center')

history_text_frame = tk.Frame(history_layer, bg = '#FE5A56', width=300, height=90)
history_text_frame.place(relx = .5, rely=.6, anchor = 'center')


history_text = tk.Label(history_text_frame, text = '', font = ('Arial', 10, 'italic'), bg = '#FE5A56', fg = '#56FAFE', height=6, justify='left', padx=15)
history_text.place(relx = .0, rely = .0, anchor = 'nw')






# Create input text.
input_link = ttk.Entry(video_info_frame, width = 45, style = 'TEntry')
input_link.place(relx = .54, rely = .15, anchor = 'w')




# Route select.

route = 'C:/'
route_open = ''

def open_file():
    global route
    global route_open
    route_open = open(rf'.\Resources\Config\route.txt', 'r+')
    route = route_open.readline()

    return route_open


open_file()

routes = [route]





features_text_title = tk.Label(download_config_layer, text = 'Video Unknown', font = ('Arial', 15, 'bold italic'), bg = '#FE5A56', fg = '#f5f5f5')
features_text_title.place(relx = .05, rely = .16, anchor = 'w')




features_text_channel = tk.Label(download_config_layer, text = 'Channel: Unknown', font = ('Arial', 10, 'italic'), bg = '#FE5A56', fg = '#f5f5f5')
features_text_channel.place(relx = .05, rely = .38, anchor = 'w')

features_text_more = tk.Label(download_config_layer, text = 'Weight and format: 0MB - ###', font = ('Arial', 10, 'italic'), bg = '#FE5A56', fg = '#f5f5f5')
features_text_more.place(relx = .05, rely = .55, anchor = 'w')


# Route text.
route_text = tk.Label(download_config_layer, text = f'Save route: {route}', font = ('Arial', 10, 'italic'), bg = '#FE5A56', fg ='#f5f5f5')
route_text.place(relx = .05, rely = .73, anchor = 'w')

restant_text = tk.Label(download_config_layer, text = f'Approximate time: 00:00', font = ('Arial', 10, 'italic'), bg = '#FE5A56', fg = '#f5f5f5')
restant_text.place(relx = .05, rely = .9, anchor = 'w')




percent_text = tk.Label(video_miniature_frame, text = f'', font = ('Arial', 4, 'italic bold'), bg = '#ffffff', fg = 'black')
percent_text.place(relx = .05, rely = .965, anchor = 'w')





# Checkbox zone.
    # Title format.
format_title = tk.Label(video_info_frame, text = 'Select a format:', font = ('Arial', 15, 'italic bold'), bg = '#FE5A56', fg = '#f5f5f5')
format_title.place(relx = .54, rely = .35,  anchor = 'w')


option_download = IntVar()

mp3_option = Radiobutton(video_info_frame, text = 'MP3', variable = option_download, value = 1)
mp3_option.configure(bg = '#FE5A56', activebackground = '#FE5A56')
mp3_option.place(relx = .8, rely = .35, anchor = 'w')


mp4_option = Radiobutton(video_info_frame, text = 'MP4', variable = option_download,
value = 2)
mp4_option.configure(bg = '#FE5A56', activebackground = '#FE5A56')
mp4_option.place(relx = .88, rely = .35, anchor = 'w')


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

browser_button = ttk.Button(video_info_frame, text = 'Folder', width = 15, command = open_route, cursor = 'plus', image = folder_icon)
browser_button.place(relx=.8, rely = .55, anchor = 'w')




# Download function  anti bug.
def download_function(): # Create new thread (bug)

    if option_download.get() == 1:

        if input_link.get() == '':
            tk.messagebox.showwarning('Warning!', 'Specify the download link.')


        elif route == 'C:/':
            tk.messagebox.showerror('¡Error!', 'Make sure to choose a path other than C:/\n(This causes permission errors)')


        elif 'https://open.spotify.com/playlist/' in input_link.get():
            a = Thread(target = lambda: audio_downloader_spotify(link_spot_playlist = input_link.get(), button = download_button, inputContent= input_link, route = route, folder_button = browser_button, frame = video_miniature, title_widget = features_text_title, channel = features_text_channel, percent_text = percent_text, restant_widget = restant_text, bytes_widget = features_text_more, checkbox_mp3 = mp3_option, checkbox_mp4 = mp4_option, list_history = downloads_history, h_text = history_text, route_miniature = './Resources/Icons/')).start()




        else:      
            a = Thread(target = lambda: audio_downloader(link_video = input_link.get(), button = download_button, inputContent= input_link, route = route, folder_button = browser_button, frame = video_miniature, title_widget = features_text_title, channel = features_text_channel, percent_text = percent_text, restant_widget = restant_text, bytes_widget = features_text_more, checkbox_mp3 = mp3_option, checkbox_mp4 = mp4_option, list_history = downloads_history, h_text = history_text, route_miniature = './Resources/Icons/')).start()




    elif option_download.get() == 2:

        if input_link.get() == '':
            tk.messagebox.showwarning('Warning!', 'Specify the download link.')


        elif route == 'C:/':
            tk.messagebox.showerror('¡Error!', 'Make sure to choose a path other than C:/\n(This causes permission errors)')

        else:
            a = Thread(target = lambda: video_downloader(link_video = input_link.get(), button = download_button, inputContent= input_link, route = route, folder_button = browser_button, frame = video_miniature, title_widget = features_text_title, channel = features_text_channel, percent_text = percent_text, restant_widget = restant_text, bytes_widget = features_text_more, checkbox_mp3 = mp3_option, checkbox_mp4 = mp4_option, list_history = downloads_history, h_text = history_text, route_miniature = './Resources/Icons/')).start()


    else:
        tk.messagebox.showwarning('Warning!', 'Choose a format in which to download your content')



download_button = ttk.Button(video_info_frame, text = 'Download', command = download_function, width = 23, cursor = 'hand1')
download_button.place(relx=.54, rely = .55, anchor = 'w')





# Menu.
menu_bar = tk.Menu(root)
root.configure(menu = menu_bar)

def config_pop():
    open_file()
    configWindow_popup(root, route, routes, route_open, open_file, './Resources/Icons/wallpaper.png')



configMenu = tk.Menu(menu_bar, tearoff = 0)
configMenu.add_command(label = 'Configure App', command = config_pop)




def aboutme_pop():
    aboutme_popup(root)



moreMenu = tk.Menu(menu_bar, tearoff = 0)
moreMenu.add_command(label = 'About Me', command = aboutme_pop)




menu_bar.add_cascade(label = 'Edit', menu = configMenu)
menu_bar.add_cascade(label = 'More', menu = moreMenu)




root.mainloop()