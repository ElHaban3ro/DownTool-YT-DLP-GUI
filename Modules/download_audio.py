from yt_dlp import YoutubeDL

import tkinter as tk
import youtube_dl

import os

from threading import Thread

import json
import urllib.request

from PIL import ImageTk, Image


def audio_downloader(button, link_video, list_history, inputContent, frame, folder_button, channel, title_widget, percent_text, restant_widget, bytes_widget, checkbox_mp3, checkbox_mp4, h_text, route = r'C:\Users\ferdh\Desktop\Projects\DownTool\Descargas test', route_miniature = r'C:\Users\ferdh\Desktop\Projects\DownTool\Descargas test'):

    video = []
    videos_list_names = []
    link_video.replace(' ', '')
    video = link_video.split(',') # Split by space (¿change?).


    if 'https://www.youtube.com/playlist?list=' in link_video:
        try:
            button['state'] = 'disabled'
            inputContent['state'] = 'disabled'
            folder_button['state'] = 'disabled'
            button['text'] = 'Get PlayList Info...'


            checkbox_mp3['state'] = 'disabled'
            checkbox_mp4['state'] = 'disabled'


            playlist_info = YoutubeDL().extract_info(link_video, download = 
            False)
            

            for i in playlist_info['entries']:
                video.append(i['webpage_url'])

            video = video[1:]

        except:
            tk.messagebox.showerror('¡Error! ñ', 'Error 404. Make sure of the following: \nThe PlayList is not private. \nThe PlayList link is correct. \nYou have an internet connection.')


    else:
        button['state'] = tk.DISABLED
        inputContent['state'] = 'disabled'
        folder_button['state'] = 'disabled'
        button['text'] = 'Get Info...'


        checkbox_mp3['state'] = 'disabled'
        checkbox_mp4['state'] = 'disabled'



    
    print(video)

    for index_video in range(len(video)):
        try:
            video_info = YoutubeDL().extract_info(f'{video[index_video]}', download = 
            False)

            name = video_info['title']

            name = name.replace('/', '-')

            button['text'] = 'Download...'

            if len(name) > 20:
                title_widget['text'] = f'{name[:20]}...'
            else:
                title_widget['text'] = f'{name}'


            channel['text'] = f'Channel: {video_info["channel"]}'

            json_video_info = json.dumps(video_info, indent = 4)
            # print(json_video_info)

            if len(video) > 1:
                videos_list_names.append(name)




            # Miniature video.
            miniature_video_link = video_info['thumbnails'][-1]['url']
            # print(miniature_video_link)

            
            miniature = open(rf'{route_miniature}/miniature.png', 'wb')
            miniature.write(urllib.request.urlopen(miniature_video_link).read())
            miniature.close()
            route_miniature = rf'{route_miniature}/miniature.png'


            put_miniature = ImageTk.PhotoImage(Image.open(route_miniature).resize((320, 180)))

            put_m = tk.Label(frame, image = put_miniature, bg = '#260b12')
            put_m.place(relx = .5, rely = .5, anchor = 'center')

            def my_hook(d):
                    if d['status'] == 'downloading':
                        p = d['_percent_str']
                        p = p.replace('%','')
                        restant_widget['text'] = f"Approximate time: {d['_eta_str']}"
                        percent_text['text'] = f"{d['_percent_str']}"
                        bytes_widget['text'] = f'Weight and format: {d["_total_bytes_str"]} - MP4'








            filename = fr'{route}\DownTool - {name}.mp3'
            options = {
                'format': 'bestaudio/best',
                'keepvideo': False,
                'outtmpl': filename,
                'progress_hooks': [my_hook]
            }

            with YoutubeDL(options) as ydl:
                d = ydl.download([video[index_video]])

                # print(f'D tiene: {d["status"]}')



            route_miniature = route


            restant_widget['text'] = f"Approximate time: 00:00"
            percent_text['text'] = f""
            bytes_widget['text'] = f'Weight and format: 0MiB - ###'

            
            os.remove(rf'{route_miniature}/miniature.png')

            


            if len(video) == 1:
                put_m = tk.Label(frame, bg = '#221e1e')
                put_m.place(relx = .5, rely = .5, anchor = 'center')

                tk.messagebox.showinfo('Process completed successfully', f'The video {name} has been downloaded successfully.')


            list_history.insert(0, name)
            h_text['text'] = ''

            for i in list_history:
                h_text['text'] = f'{h_text["text"] + i}\n'
                

            print(list_history)


        except:
            
            tk.messagebox.showerror('¡Error 404!', 'Error 404. (Error downloading the video, make sure you have internet and have the correct link and try again)')


    if len(video) > 1 and len(videos_list_names) > 0:
            tk.messagebox.showinfo('Process completed successfully', f'All videos in the list have been downloaded: {videos_list_names}')
    

            # button['state'] = 'normal'
            # inputContent['state'] = 'normal'
            # folder_button['state'] = 'normal'
            # button['text'] = 'Download'
            # inputContent.delete(0, 'end')
            

    put_m = tk.Label(frame, bg = '#260b12', width = 320, height = 180)
    put_m.place(relx = .5, rely = .5, anchor = 'center')
    

    print(f'Se Ha hecho la descarga de: {video}')
    button['state'] = tk.NORMAL
    button['text'] = 'Download'
    title_widget['text'] = 'Unknown Video'
    channel['text'] = f'Channel: Unknown'
    inputContent['state'] = 'normal'
    inputContent.delete(0, 'end')

    folder_button['state'] = 'normal'
    
    checkbox_mp3['state'] = 'normal'
    checkbox_mp4['state'] = 'normal'
    

    # except:
    #     tk.messagebox.showerror('¡Error 404!', 'Error 404. (Error downloading the video, make sure you have internet and have the correct link and try againaaaaaaaaaaaaaaaaaaaaaaaaaaaaa)')
    #     button['state'] = 'normal'
    #     inputContent['state'] = 'normal'
    #     folder_button['state'] = 'normal'
    #     button['text'] = 'Download'
    #     inputContent.delete(0, 'end')
