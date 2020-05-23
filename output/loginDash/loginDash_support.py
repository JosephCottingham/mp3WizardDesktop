import sys

from requests import HTTPError

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
import uploadBookDash_support
from firebase import Firebase

def login():
    config = {
        "apiKey": "AIzaSyDr3GgNZ7hJhhXb9Grys6xrTRRFsWJlQGA",
        "authDomain": "mp3wizard-466b5.firebaseapp.com",
        "databaseURL": "https://mp3wizard-466b5.firebaseio.com",
        "storageBucket": "mp3wizard-466b5.appspot.com"
    }

    firebase = Firebase(config)
    auth = firebase.auth()

    w.emailEntry.configure(state="disabled")
    w.passwordEntry.configure(state="disabled")
    try:
        user = auth.sign_in_with_email_and_password(w.emailEntry.get(), w.passwordEntry.get())
        validUser = True
    except HTTPError:
        print(str(HTTPError.__text_signature__))
        w.emailEntry.configure(state="normal")
        w.passwordEntry.configure(state="normal")
        w.errorLabel.configure(text="Error when attempting to login")
        w.errorLabel.configure(foreground='#FF0000')
        sys.stdout.flush()
    if validUser:
        print(user)
        print(type(user))
        destroy_window()
        uploadBookDash_support.start(user)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import loginDash
    loginDash.vp_start_gui()




