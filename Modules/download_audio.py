# Thrid modules.
import time
from urllib.error import HTTPError
import music_tag
from yt_dlp import YoutubeDL
from PIL import ImageTk, Image
import tkinter as tk
import os
from threading import Thread
import json
import urllib.request

import re



def audio_downloader(button, link_video, list_history, inputContent, frame, folder_button, channel, title_widget, percent_text, percent_bar_obj, restant_widget, bytes_widget, checkbox_mp3, checkbox_mp4, h_text, route = r'C:\Users\ferdh\Desktop\Projects\DownTool\Descargas test', route_miniature = r'C:\Users\ferdh\Desktop\Projects\DownTool\Descargas test'):

    video = []
    videos_list_names = []
    link_video.replace(' ', '')
    video = link_video.split(',') # Split by space (¿change?).



    if 'https://www.youtube.com/playlist?list=' in link_video:
        try:
            button['state'] = 'disabled'
            inputContent['state'] = 'disabled'
            folder_button['state'] = 'disabled'
            button['text'] = 'Get Playlist Info...'

            percent_bar_obj['mode'] = 'indeterminate'
            percent_bar_obj.start(10)




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

        percent_bar_obj['mode'] = 'indeterminate'
        percent_bar_obj.start(10)



        checkbox_mp3['state'] = 'disabled'
        checkbox_mp4['state'] = 'disabled'





    
    print(video)

    for index_video in range(len(video)):
        # try:
        if True:

            video_info = YoutubeDL().extract_info(f'{video[index_video]}', download = 
            False)


            name = video_info['title']

            name = name.replace('/', '-')
            name = name.replace(':', '-')




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




            try:
                # Miniature video.

                # 35 funciona, pero es una resolución bastante extraña.
                if len(video_info['thumbnails']) == 46:
                    miniature_video_link = video_info['thumbnails'][-1]['url']
                
                else:
                    miniature_video_link = video_info['thumbnails'][30]['url']
    
                miniature = open(rf'{route_miniature}/miniature.png', 'wb')
                miniature.write(urllib.request.urlopen(miniature_video_link).read())
                miniature.close()
                route_miniature_edit = rf'{route_miniature}/miniature.png'



                miniature_recode = Image.open(route_miniature_edit).resize((320, 180))

                miniature_recode.save(f'{route_miniature}/miniature.png')


                put_miniature = ImageTk.PhotoImage(Image.open(route_miniature_edit))

                put_m = tk.Label(frame, image = put_miniature, bg = '#260b12')
                put_m.place(relx = .5, rely = .5, anchor = 'center')


            except HTTPError:
                miniature.close()
                # Miniature video error
                route_miniature_edit = rf'Resources/Icons/error.miniature.png'


                put_miniature = ImageTk.PhotoImage(Image.open(route_miniature_edit).resize((320, 180)))

                put_m = tk.Label(frame, image = put_miniature, bg = '#260b12')
                put_m.place(relx = .5, rely = .5, anchor = 'center')
                pass
            
            




            percent_bar_obj.stop()
            percent_bar_obj['mode'] = 'determinate'

            def my_hook(d):
                    if d['status'] == 'downloading':
                        p = d['_percent_str']
                        p = p.replace('%','')
                        restant_widget['text'] = f"Approximate time: {d['_eta_str']}"
                        percent_text['text'] = f"{d['_percent_str']}"
                        bytes_widget['text'] = f'Weight and format: {d["_total_bytes_str"]} - MP4'

                        p = re.sub(r'\033\[(\d|;)+?m', '', p)
                        p = float(p)

                        percent_bar_obj['value'] = p






            name = name.replace('¿', '')
            name = name.replace('"', '')
            name = name.replace('?', '#')



            filename = fr'{route}\[DT] - {name}.mp3'
            options = {
                    'format': '140',
                    'keepvideo': False,
                    'outtmpl': filename,
                    'progress_hooks': [my_hook],
                    'noplaylist': True,
                    'acodec': 'Opus'
            }

            with YoutubeDL(options) as ydl:
                d = ydl.download([video[index_video]])

            percent_bar_obj['value'] = 0.0


                



            route_m = route.replace('/', r"\\")
            route_m = route_m.split(r'\\')

            route_new = []

            for e, i in enumerate(route_m):
                if e == 1:
                    route_new.append(fr'\{i}')

                else:
                    route_new.append(i)



            route_m = os.path.join(*route_new)
            name_m = name.replace('|', '#')

            route_m = route_m + fr'\[DT] - {name_m}.mp3'

            route_m = str(route_m)

            

            
            button['text'] = 'Editing metadata...'

            song = music_tag.load_file(route_m)

            song['artist'] = video_info["channel"]
            song['album'] = 'DownTool Youtube'

            

            if route_miniature_edit != f'Resources/Icons/error.miniature.png':
    
                print(route_miniature_edit)
                cover = open(route_miniature_edit, 'rb')


                song['artwork'] = cover.read()


                cover.close()


            song.save()




            restant_widget['text'] = f"Approximate time: 00:00"
            percent_text['text'] = f""
            bytes_widget['text'] = f'Weight and format: 0MiB - ###'

            




            


            if len(video) == 1:
                put_m = tk.Label(frame, bg = '#221e1e')
                put_m.place(relx = .5, rely = .5, anchor = 'center')

                tk.messagebox.showinfo('Process completed successfully', f'The video {name} has been downloaded successfully.')


            list_history.insert(0, name)
            h_text['text'] = ''

            for i in list_history:
                h_text['text'] = f'{h_text["text"] + i}\n'
                

            print(list_history)

        # except:
            
        #     tk.messagebox.showerror('¡Error 404!', 'Error 404. (Error downloading the video, make sure you have internet and have the correct link and try again)')


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
    

    try:
        if route_miniature_edit != f'Resources/Icons/error.miniature.png':
                    os.remove(rf'{route_miniature_edit}')

    except:
        pass


    button['state'] = tk.NORMAL
    button['text'] = 'Download'
    title_widget['text'] = 'Unknown Video'
    channel['text'] = f'Channel: Unknown'
    inputContent['state'] = 'normal'
    inputContent.delete(0, 'end')

    folder_button['state'] = 'normal'
    
    checkbox_mp3['state'] = 'normal'
    checkbox_mp4['state'] = 'normal'