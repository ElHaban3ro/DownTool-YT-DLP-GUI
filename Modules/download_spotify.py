# Thrid modules.
from itertools import count
from PIL import ImageTk, Image
import tkinter as tk
import os
import json
import urllib.request
import music_tag


from urllib.error import HTTPError

# Spotify modules
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from yt_dlp import YoutubeDL

# Spotify connect.
print('Connecting to spotify...\n\n\n')

client_creds = SpotifyClientCredentials(client_id = 'ef383dcde5dd4626bea8ea91245ffb81', client_secret = 'e5a520696f064f31ad15d715ffc495df')
client = spotipy.Spotify(client_credentials_manager = client_creds)

print('Connected to spotify.\n\n\n\n\n')













def audio_downloader_spotify(button, link_spot_playlist, list_history, inputContent, frame, folder_button, channel, title_widget, percent_text, restant_widget, bytes_widget, checkbox_mp3, checkbox_mp4, h_text, route = r'C:\Users\ferdh\Desktop\Projects\DownTool\Descargas test', route_miniature = r'C:\Users\ferdh\Desktop\Projects\DownTool\Descargas test'):


    songs = []
    songs_urls_yt = []
    videos_list_names = []



    if 'https://open.spotify.com/playlist/' in link_spot_playlist:

        # try:

        if True:
            main_artists = []
            album_names = []
            cover_urls = []
            covers_routes = []



            button['state'] = 'disabled'
            inputContent['state'] = 'disabled'
            folder_button['state'] = 'disabled'
            button['text'] = 'Get Spotify Playlist Info...'

            

            checkbox_mp3['state'] = 'disabled'
            checkbox_mp4['state'] = 'disabled'


            consult = client.playlist_tracks(link_spot_playlist)
            total_playlist = consult['total']

            jumps = [*range(0, total_playlist, 100)]

            if jumps[-1] != total_playlist:
                res = (total_playlist - jumps[-1]) + jumps[-1]
                jumps.append(res)



            for i in jumps[:-1]:
                playlist_info = client.playlist_tracks(link_spot_playlist, offset = i)
                


                playlist_info = [playlist_info['items']]
                
                for i in playlist_info[0]:
                    try:
                    # if True:

                        song_artists = ''

                        print(i['track']['name'])


                        song_name = i["track"]["name"]

                        artists = []
                        

                        for a in i['track']['artists']:
                            song_artists = song_artists + f"{a['name']} - "


                            artists.append(a['name'])

                        song_artists = song_artists[:-2]
                        songs.append(f'{song_artists}, {song_name}')


                        main_artists.append(artists)

                        # https://open.spotify.com/playlist/1YJGvUgssQrppULzfE8l2a

                        album_names.append(i['track']['album']['name'])
                        cover_urls.append(i['track']['album']['images'][0]['url'])

                                                    

                    except TypeError as err:
                        print(err)
                        pass


            # button['text'] = 'Spotify Covers Download...'
            
            # for cc, cover_link in enumerate(cover_urls):
            #     cover_name = rf'{route_miniature}/{cc}.png'
            #     covers_routes.append(cover_name)

            #     cover = open(rf'{route_miniature}/{cc}.png', 'wb')
            

            #     cover.write(urllib.request.urlopen(cover_link).read())
            #     cover.close()






            # count_songs = 0

            for count_songs, song in enumerate(songs):
                    
                playlist_info = YoutubeDL().extract_info(f'ytsearch:{song}', download = False)

                link_song_spot = playlist_info

                try:
                # if True:
                    
                    for i in link_song_spot['entries']:

                        video_info = YoutubeDL().extract_info(f'{i["webpage_url"]}', download = False)

                        quality_list = []

                        for quality_count in range(len(video_info['formats'])):

                            if 'audio only' in video_info['formats'][quality_count]['format']:

                                quality_list.append(video_info['formats'][quality_count]['format'])






                        name = video_info['title']
                        name = name.replace('/', '-')
                        button['text'] = 'Download...'

                        if len(name) > 20:
                            title_widget['text'] = f'{name[:20]}...'
                        else:
                            title_widget['text'] = f'{name}'




                        channel['text'] = f'Channel: {video_info["channel"]}'
                        songs_urls_yt.append(i['webpage_url'])



                        videos_list_names.append(name)




                        try:
                            cover_name = f'{route_miniature}/{count_songs}.png'
                            covers_routes.append(cover_name)

                            cover = open(f'{route_miniature}/{count_songs}.png', 'wb')
                        

                            cover.write(urllib.request.urlopen(cover_urls[count_songs]).read())
                            cover.close()




                            put_miniature = ImageTk.PhotoImage(Image.open(f'{route_miniature}/{count_songs}.png').resize((180, 180)))

                            put_m = tk.Label(frame, image = put_miniature, bg = '#260b12')
                            put_m.place(relx = .5, rely = .5, anchor = 'center')


                        except HTTPError:
                            put_miniature = ImageTk.PhotoImage(Image.open(rf'Resources/Icons/error.miniature.png').resize((320, 180)))

                            put_m = tk.Label(frame, image = put_miniature, bg = '#260b12')
                            put_m.place(relx = .5, rely = .5, anchor = 'center')
                            pass


                        def my_hook(d):
                                if d['status'] == 'downloading':
                                    p = d['_percent_str']
                                    p = p.replace('%','')
                                    restant_widget['text'] = f"Approximate time: {d['_eta_str']}"
                                    percent_text['text'] = f"{d['_percent_str']}"
                                    bytes_widget['text'] = f'Weight and format: {d["_total_bytes_str"]} - MP4'



                        print(quality_list)

                        filename = fr'{route}\[DT Spotify] - {name}.mp3'
                        options = {
                            'format': '140',
                            'keepvideo': False,
                            'outtmpl': filename,
                            'progress_hooks': [my_hook],
                            'noplaylist': True,
                            'acodec': 'Opus'
                        }

                        with YoutubeDL(options) as ydl:
                            d = ydl.download(i['webpage_url'])








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

                        route_m = route_m + fr'\[DT Spotify] - {name_m}.mp3'

                        route_m = str(route_m)

                        # r = os.path.join(route_m)


                        song = music_tag.load_file(route_m)

                        song['artist'] = main_artists[count_songs][0]
                        song['album'] = album_names[count_songs]

                        print(covers_routes[count_songs])


                        img = open(covers_routes[count_songs], 'rb')


                        song['artwork'] = img.read()


                        img.close()


                        song.save()
                        os.remove(covers_routes[count_songs])



                        list_history.insert(0, name)
                        h_text['text'] = ''

                        for i in list_history:
                            h_text['text'] = f'{h_text["text"] + i}\n'

                        # count_songs += 1




# https://open.spotify.com/playlist/1YJGvUgssQrppULzfE8l2a



                       





                        restant_widget['text'] = f"Approximate time: 00:00"
                        percent_text['text'] = f""
                        bytes_widget['text'] = f'Weight and format: 0MiB - ###'

                        

                except:
                    tk.messagebox.showerror('¡Error 404!', 'Error 404. (Error downloading the playlist, make sure you have internet and have the correct link and try again)')


        # except:
        #     tk.messagebox.showerror('¡Error! ñ', 'Error 404. Make sure of the following: \nThe PlayList is not private. \nThe PlayList link is correct. \nYou have an internet connection.')



        if len(videos_list_names) >= 1:
            tk.messagebox.showinfo('Process completed successfully', f'All videos in the list have been downloaded: {videos_list_names}')
            


        put_m = tk.Label(frame, bg = '#260b12', width = 320, height = 180)
        put_m.place(relx = .5, rely = .5, anchor = 'center')
        
        try:
            os.remove(rf'{route_miniature}/miniature.png')
        except:
            pass


        print(f'Se Ha hecho la descarga de tu Playlist!')
        button['state'] = tk.NORMAL
        button['text'] = 'Download'
        title_widget['text'] = 'Unknown Video'
        channel['text'] = f'Channel: Unknown'
        inputContent['state'] = 'normal'
        inputContent.delete(0, 'end')

        folder_button['state'] = 'normal'
        
        checkbox_mp3['state'] = 'normal'
        checkbox_mp4['state'] = 'normal'