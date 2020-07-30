# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:08:40 2020

@author: puroh
"""


from pytube import YouTube
from youtube_search import YoutubeSearch
import tkinter as tk
from tkinter import messagebox

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 600, height = 90)
canvas1.pack()

entry1 = tk.Entry (root, width = 90) 
canvas1.create_window(300, 20, window=entry1)

def download ():  
    
    search_term = entry1.get()
    results = YoutubeSearch(str(search_term), max_results=1).to_dict()
    print("..........................................................................check 1")
    link_suffix = results[0]['url_suffix']
    print("..........................................................................check 2")
    link = 'https://www.youtube.com/' + link_suffix
    print("..........................................................................check 3")
    
    SAVE_PATH = "C:/Users/puroh/Music/youtube_dowload/"
    # try: 
    #object creation using YouTube which was imported in the beginning 
    yt = YouTube(url = link)  
    # except: 
        # messagebox.showinfo("Error", "connection error!!")
    
    # mp4files = yt.filter('mp4') 
    vid = yt.streams.filter(file_extension = "mp4")
    # print(vid)
    # yt.set_filename(str(search_term))
    d_video = vid.get_by_itag(18)
    # print(d_video)
    try: 
    #downloading the video 
        d_video.download(SAVE_PATH) 
    except: 
        messagebox.showinfo("Error", "Check connection!!")
    messagebox.showinfo("Task", "Downloaded!!")
    
    
button1 = tk.Button(text='Download', command=download)
canvas1.create_window(300, 50, window=button1)

root.mainloop()