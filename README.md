
# DownTool (YouTube Videos Downloader, NO ADS)


Welcome to DownTool, a tool to **download** videos from youtube in mass or single. If you want to pass several videos to download, it is important to pass the links separated by commas.

The **App** is developed with the **Tkinter** graphical interface library and using **yt-dlp** to download the videos. The formats in which the videos are downloaded are in **MP3** format for audio, and **MP4** for video. As for the quality of the videos and audios, the best of the **videos/audios** is always taken, this can be easily changed by accessing the **quality** of the videos and in the download modules, change the format. Somewhere in the download modules there is a print **(commented)** for you to get the qualities, this thing about choosing the qualities because it really isn't what **I need**.


This app was developed with the aim of being able to download videos from YouTube en **masse** without having to deal with pages full of advertising. Do you want to improve it? Go ahead :) Fork
## Authors

- [@ElHaban3ro](https://www.github.com/ElHaban3ro)
- [Discord](https://discord.gg/9jbB6wnqX3)


## Download Executable

- [Download Windows!](https://github.com/ElHaban3ro/DownTool-YT-DLP-GUI/blob/main/DownTool%201.2WIN-PORT.zip?raw=true)
- Download Linux (Not available)




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