import sys
import os
from pathlib import Path
from tkinter import filedialog as fd
import numpy as np
import time

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from firebase import Firebase

def addFileToList():
    path = str(fd.askopenfilename(initialdir=str(Path.home())))
    if path != '':
        if w.TEntry1.get() == '':
            name = path.split('/')[-1].split('.')[0]
            w.TEntry1.insert(0, name)
        filePathNPTemp = np.append(filePathNP, [path])
        resetScrolledFileList(filePathNPTemp)
        sys.stdout.flush()

def resetScrolledFileList(filePathNPTemp):
    w.scrolledFileList.delete(0,filePathNPTemp.size)
    x = 0
    print(filePathNPTemp)
    for item in filePathNPTemp:
        name = item.split('/')
        w.scrolledFileList.insert(x, str(name[-1]))
        x=x+1
    global filePathNP
    filePathNP = filePathNPTemp


def clearScrolledFileList():
    print('uploadBookDash_support.clearScrolledFileList')
    w.scrolledFileList.delete(0,filePathNP.size)
    sys.stdout.flush()

def upload():
    config = {
        "apiKey": "AIzaSyDr3GgNZ7hJhhXb9Grys6xrTRRFsWJlQGA",
        "authDomain": "mp3wizard-466b5.firebaseapp.com",
        "databaseURL": "https://mp3wizard-466b5.firebaseio.com",
        "storageBucket": "mp3wizard-466b5.appspot.com"
    }

    firebase = Firebase(config)
    storage = firebase.storage()
    for x in range(filePathNP.size):
        ext = '.' + filePathNP[x].split('.')[-1]
        loc = "users/{0}/{1}/{2}".format(user['localId'], str(w.TEntry1.get()), str(x+1)+ext)
        print(loc)
        storage.child(loc).put(str(filePathNP[x]), user['idToken'])

    database = firebase.database()
    data = {"title": str(w.TEntry1.get()), "fileNum":str(filePathNP.size), "locSec":"0", "currentFile":"1",  "downloaded":"Cloud"}
    database.child(user['localId']).child(str(w.TEntry1.get())).set(data, user['idToken'])
    print('uploadBookDash_support.upload')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    w.TLabel1.configure(text=user['email'])

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def start(u):
    global user, filePathNP
    filePathNP = np.array([])
    user = u
    import uploadBookDash
    uploadBookDash.vp_start_gui()




