#!/usr/bin/env python3

from __future__ import unicode_literals
import youtube_dl
import urllib.request
import webbrowser
from tkinter import *
from PIL import Image, ImageTk

global txt

txt = ""

def window():
    root = Tk()
    root.resizable(False, False)
    root.title("Youtube Downloader")

    bgimg = ImageTk.PhotoImage(Image.open('images/background.jpg'))
    root.geometry("%dx%d+50+30" % (bgimg.width(), bgimg.height()))

    cv = Canvas(width=bgimg.width(), height=bgimg.height())
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(0, 0, image=bgimg, anchor='nw')

    img = ImageTk.PhotoImage(Image.open('images/icon.png').resize((250,250)))
    lbimg = cv.create_image(bgimg.width()/4 + 10, 0, image = img, anchor='nw')

    input = Entry(cv, width = 50, justify = 'center')
    input.insert(0, 'Enter Youtube URL'); input.focus_set()
    input.pack(); cv.create_window(250, 200, window=input)

    btnDownload = Button(cv, text="Download", command = lambda: downloader(input.get()), bg = 'gold')
    btnDownload.pack(padx=10, pady=5); cv.create_window(150, 270, window=btnDownload)

    btnOpen = Button(cv, text="Open in Browser", command = lambda: open(input.get()), bg = 'tan1')
    btnOpen.pack(padx=10, pady=5); cv.create_window(320, 270, window=btnOpen)

    btnQuit = Button(cv, text="Quit", command=root.destroy, bg = 'firebrick1')
    btnQuit.pack(side='right', padx=10, pady=5, anchor='se')

    root.mainloop()

def downloader(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        ydl.download([url])



def open(url):
    webbrowser.open(url)

if __name__ == '__main__':
    window()
