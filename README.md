
# DownTool (YouTube Videos Downloader, NO ADS)



Welcome to DownTool, a tool to **download** youtube videos in bulk or individually. 

The **App** is developed with the **Tkinter** GUI library and uses **yt-dlp** to download the videos. The formats in which the videos are downloaded are **MP3** format for audio, and **MP4** for video. As for the quality of the videos and audios, the best of the **videos/audios** is always taken, this can be easily changed by accessing the **quality** of the videos and in the download modules, change the format. Somewhere in the download modules there is a **(commented)** printout for you to get the qualities, this is not really what I **need**.


This app was developed with the goal of being able to download YouTube videos in **mass** without having to deal with pages full of ads. Do you want to improve it? Go ahead :) Fork

<<<<<<< HEAD
## (1.3) What's new?
- Now, support for downloading your spotify playlists
- Support for youtube playlist.
- Fixed several VERY important bugs.


## UPDATE 1.4.5

=======
## (1.4) What's new?
>>>>>>> aee975f9b20b205ac1ee95e84743bc1c66be36ef
Update contain:

- Now, when you download your **Spotify** playlists, they will include metadata: *The Cover*, *Album* and *Artist*!

- This version does not come with an executable because I will soon update to add metadata to the other *download methods*!

- Fixed the location of the temporary *thumbnail*!

- Metadata in ***all formats***!

- Some bugs fixed!

- Temporary thumbnail location moved !

![Example Update](./example_update_1.4.5.jpg)




## ¿How Work?

It is quite easy. The program prompts you for an ***input***, where you will enter your **link**. 


You can do this either as a single link:

```
https://www.youtube.com/watch?v=-KkX7UVdTN8
```
---
Or several links separated by commas:
```
https://www.youtube.com/watch?v=nDZvMKfrzaM, https://www.youtube.com/watch?v=Mmp2gFwZXPs, https://www.youtube.com/watch?v=35Ui0XAkwmc, https://www.youtube.com/watch?v=SgnJdGXB3lE
```
---
If your ***case*** is to download even more massive videos, you can try passing the link of a public ***playlist***:

```
https://www.youtube.com/playlist?list=PLzuFY9Ixj9Z6nf7z6t5YmPDTLBgksk8Ts
```
---
Or, if you prefer to download your favorite playlists from Spotify, just leave us your link!
```
https://open.spotify.com/playlist/03faf9Q9OSxLcfrtax9Wjn
```

## Author Contact

- [GitHub Profile @ElHaban3ro](https://www.github.com/ElHaban3ro)
- [Discord ! Die()#1274 or click here to join server!](https://discord.gg/9jbB6wnqX3)
- [Twitter @ElHaban3ro](https://twitter.com/ElHaban3ro)


## Download Executable

- [Download Windows!](https://github.com/ElHaban3ro/DownTool-YT-DLP-GUI/blob/main/DownTool%201.4.5WIN-PORTABLE.zip?raw=true)
- Download iMac! (Coming Soon)
- Download Linux! (Coming Soon)




## Installation

Use pip to install requirements

```bash
  pip install -r requirements.txt
```
    
To run the program in development mode, once the requirements have been installed, simply run the DownApp.py file

---

If you want to create a package for your operating system, use the command:

```bash
  pyinstaller --windowed --icon=./Resources/Icons/DownTool_2.ico DownApp.py
```

And then move the ***Resources*** folder to ***dist/DownApp/***.

We do this so that the resources like images or fonts work correctly. Once this is done you can use the executable.Next, you can remove the folder from the ***dist*** directory and delete these two: ***dist*** and ***build***.
