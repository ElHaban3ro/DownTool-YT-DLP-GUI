# from youtube_dl import YoutubeDL
import threading
from yt_dlp import YoutubeDL

import tkinter as tk
import youtube_dl

import os

import json
import urllib.request

from PIL import ImageTk, Image

import queue


def playlist_download(playlist_link:str):

    playlist = playlist_link # Playlits link
