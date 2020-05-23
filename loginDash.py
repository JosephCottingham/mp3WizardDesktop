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

class EntryWithPlaceholder(ttk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', hint=''):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = '#000000'

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.showVal=hint

        self.put_placeholder()

    def put_placeholder(self):
        self.configure(show='')
        self.insert(0, self.placeholder)
        self['foreground'] = self.placeholder_color

    def foc_in(self, *args):
        self.configure(show=self.showVal)
        self.delete('0', 'end')
        self['foreground'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file="simpleicon.png"))
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
        foregroundColor = '#000000'
        backgroundColor = '#ffffff'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=backgroundColor)
        self.style.configure('.',foreground=foregroundColor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', foregroundColor), ('active',backgroundColor)])

        top.geometry("450x300+530+250")
        top.resizable(0, 0)
        top.title("MP3Wizard")
        top.configure(highlightcolor="black")
        top.configure(bg=backgroundColor)

        self.emailEntry = EntryWithPlaceholder(top, "EMAIL")
        self.emailEntry.place(relx=0.164, rely=0.213, relheight=0.1, relwidth=0.6)
        self.emailEntry.configure(takefocus="")
        self.emailEntry.configure(cursor="xterm")


        self.passwordEntry = EntryWithPlaceholder(top, "PASSWORD", hint='*')
        self.passwordEntry.place(relx=0.164, rely=0.45, relheight=0.1, relwidth=0.6)
        self.passwordEntry.configure(takefocus="")
        self.passwordEntry.configure(cursor="xterm")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=backgroundColor,fg=foregroundColor)
        top.configure(menu = self.menubar)

        self.loginBtn = ttk.Button(top)
        self.loginBtn.place(relx=0.2, rely=0.6, height=70, width=224)
        self.loginBtn.configure(command=loginDash_support.login)
        self.loginBtn.configure(takefocus="")
        self.loginBtn.configure(text='''Login''')

        self.errorLabel = ttk.Label(top)
        self.errorLabel.place(relx=0.1, rely=0.882, height=34, width=300)
        self.errorLabel.configure(background=backgroundColor)
        self.errorLabel.configure(foreground="#000000")
        self.errorLabel.configure(font="TkDefaultFont")
        self.errorLabel.configure(anchor="center")
        self.errorLabel.configure(relief="flat")
        self.errorLabel.configure(text='''Please enter account info''')


if __name__ == '__main__':
    vp_start_gui()







