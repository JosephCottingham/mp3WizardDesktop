import sys

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

import loginDash_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    loginDash_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    loginDash_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1095x442+3030+592")
        top.minsize(1, 1)
        top.maxsize(6825, 2130)
        top.resizable(0, 0)
        top.title("New Toplevel")
        top.configure(highlightcolor="black")

        self.emailEntry = ttk.Entry(top)
        self.emailEntry.place(relx=0.164, rely=0.213, relheight=0.133
                , relwidth=0.789)
        self.emailEntry.configure(takefocus="")
        self.emailEntry.configure(cursor="xterm")

        self.emailLabel = ttk.Label(top)
        self.emailLabel.place(relx=0.065, rely=0.213, height=56, width=101)
        self.emailLabel.configure(background="#d9d9d9")
        self.emailLabel.configure(foreground="#000000")
        self.emailLabel.configure(font="TkDefaultFont")
        self.emailLabel.configure(relief="flat")
        self.emailLabel.configure(text='''Email:''')

        self.TLabel2 = ttk.Label(top)
        self.TLabel2.place(relx=0.457, rely=0.024, height=64, width=81)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''Login''')

        self.passwordEntry = ttk.Entry(top)
        self.passwordEntry.place(relx=0.164, rely=0.45, relheight=0.133
                , relwidth=0.789)
        self.passwordEntry.configure(takefocus="")
        self.passwordEntry.configure(cursor="xterm")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.passwordLabel = ttk.Label(top)
        self.passwordLabel.place(relx=0.027, rely=0.45, height=56, width=141)
        self.passwordLabel.configure(background="#d9d9d9")
        self.passwordLabel.configure(foreground="#000000")
        self.passwordLabel.configure(font="TkDefaultFont")
        self.passwordLabel.configure(relief="flat")
        self.passwordLabel.configure(text='''Password:''')

        self.loginBtn = ttk.Button(top)
        self.loginBtn.place(relx=0.402, rely=0.687, height=83, width=224)
        self.loginBtn.configure(command=loginDash_support.login)
        self.loginBtn.configure(takefocus="")
        self.loginBtn.configure(text='''Login''')

        self.errorLabel = ttk.Label(top)
        self.errorLabel.place(relx=0.274, rely=0.882, height=34, width=511)
        self.errorLabel.configure(background="#d9d9d9")
        self.errorLabel.configure(foreground="#000000")
        self.errorLabel.configure(font="TkDefaultFont")
        self.errorLabel.configure(relief="flat")
        self.errorLabel.configure(text='''Please enter account info''')


if __name__ == '__main__':
    vp_start_gui()





