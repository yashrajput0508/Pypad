import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
class GUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Python GUI")
        self.menus()
        self.frame()
        self.scroll()
        self.bind()
        self.shortcut()
    def menus(self):
        self.menubar = Menu(self.win)
        self.win.configure(menu=self.menubar)
        self.file = Menu(self.menubar, tearoff=0)
        self.file.add_command(label="New",accelerator="Ctrl+N",compound=LEFT,command=self.new)
        self.file.add_separator()
        self.file.add_command(label="Open",accelerator="Ctrl+O",command=self.open)
        self.file.add_command(label="Save",accelerator="Ctrl+S",command=self.save)
        self.file.add_command(label="Save as",command=self.save_as)
        self.file.add_command(label="Exit",accelerator="Ctrl+Q",command=self.exit)
        self.menubar.add_cascade(label="File", menu=self.file)
        self.Edit = Menu(self.menubar, tearoff=0)
        self.Edit.add_command(label="Undo",accelerator="Ctrl+Z")
        self.Edit.add_command(label="Redo",accelerator="Ctrl+Y")
        self.Edit.add_separator()
        self.Edit.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
        self.Edit.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
        self.Edit.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
        self.Edit.add_separator()
        self.Edit.add_command(label="Find", accelerator="Ctrl+F",command=self.find)
        self.Edit.add_command(label="Select All",accelerator="Ctrl+A",command=self.select)
        self.menubar.add_cascade(label="Edit",menu=self.Edit)
        self.View=Menu(self.menubar,tearoff=0)
        self.show1=tk.IntVar()
        self.show2=tk.IntVar()
        self.show3=tk.IntVar()
        self.View.add_checkbutton(label="Show Line Numbers",variable=self.show1,command=self.update_line_number)
        self.View.add_checkbutton(label="Show Info Bar",variable=self.show2,command=self.show_info_bar)
        self.View.add_checkbutton(label="Highlight current line",variable=self.show3,command=self.highlight)
        self.underview=Menu(self.View,tearoff=0)
        self.radio=tk.IntVar()
        self.radio.set(1)
        self.underview.add_radiobutton(label="1.Default White",variable=self.radio,value=1,command=self.theme)
        self.underview.add_radiobutton(label="2.GreyGarious Grey", variable=self.radio, value=2,command=self.theme)
        self.underview.add_radiobutton(label="3.Vivacious Violet", variable=self.radio, value=3,command=self.theme)
        self.underview.add_radiobutton(label="4.Light Green", variable=self.radio, value=4,command=self.theme)
        self.underview.add_radiobutton(label="5.Solarised", variable=self.radio, value=5,command=self.theme)
        self.underview.add_radiobutton(label="6.Boisterous Blue", variable=self.radio, value=6,command=self.theme)
        self.underview.add_radiobutton(label="7.School Green", variable=self.radio, value=7,command=self.theme)
        self.View.add_cascade(label="Themes",menu=self.underview)
        self.menubar.add_cascade(label="View",menu=self.View)
        self.Help=Menu(self.menubar,tearoff=0)
        self.Help.add_command(label="About",command=self.about)
        self.Help.add_command(label="Help",command=self.help)
        self.menubar.add_cascade(label="About",menu=self.Help)
    def shortcut(self):
        self.cmenu = Menu(self.textPad,tearoff=0)
        for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
            cmd = eval("self."+i)
            self.cmenu.add_command(label=i.title(), compound=LEFT, command=cmd)
        self.cmenu.add_separator()
        self.cmenu.add_command(label='Select All', underline=7,
                              command=self.select_all)
    def bind(self):
        self.textPad.bind('<Control-N>', self.new)
        self.textPad.bind('<Control-n>', self.new)
        self.textPad.bind('<Control-O>', self.open)
        self.textPad.bind('<Control-o>', self.open)
        self.textPad.bind('<Control-S>', self.save)
        self.textPad.bind('<Control-s>', self.save)
        self.textPad.bind('<Control-A>', self.select_all)
        self.textPad.bind('<Control-a>', self.select_all)
        self.textPad.bind('<Control-x>', self.cut)
        self.textPad.bind('<Control-X>', self.cut)
        self.textPad.bind('<Control-V>', self.paste)
        self.textPad.bind('<Control-v>', self.paste)
        self.textPad.bind('<Control-C>', self.copy)
        self.textPad.bind('<Control-c>', self.copy)
        self.textPad.bind('<Control-Q>', self.exit)
        self.textPad.bind('<Control-q>', self.exit)
        self.textPad.bind('<Control-f>', self.find)
        self.textPad.bind('<Control-F>', self.find)
        self.textPad.bind('<KeyPress-F1>', self.about)
        self.textPad.bind("<Button-3>", self.popup)
    def popup(self,event):
        self.cmenu.tk_popup(event.x_root, event.y_root, 0)
    def select_all(self,event):
        self.textPad.tag_add('sel','1.0',END)
    def new(self,event):
        self.win.title("Untitled")
        self.textPad.delete('1.0',END)
        self.fh=None
    def open(self,event):
        self.filename=filedialog.askopenfilename(defaultextension='.txt',filetypes =[("All Files","*.*"),("Text Documents","*.txt")])
        if self.filename=='':
            filename=None
        else:
            self.win.title(os.path.basename(self.filename) + " - pyPad")  #
            # Returning the basename of 'file'
            self.textPad.delete(1.0, END)
            self.fh = open(self.filename, "r")
            self.textPad.insert(1.0, self.fh.read())
            self.fh.close()
    def save(self,event):
        try:
            self.fh=open(self.filename,'w')
            letter=self.textPad.get()
            self.fh.write(letter)
            self.fh.close()
        except:
            self.save_as()
    def save_as(self,event):
        try:
            # Getting a filename to save the file.
            f = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files"," *.* "),("Text Documents"," *.txt")])
            fh = open(f, 'w')
            textoutput = self.textPad.get(1.0, END)
            fh.write(textoutput)
            fh.close()
            self.win.title(os.path.basename(f) + " - pyPad")
        except:
            pass
    def exit(self,event):
        if messagebox.askokcancel("Python GUI","You want to really exit"):
            self.win.destroy()
    def cut(self,event):
        self.textPad.event_generate('<<Cut>>')
    def copy(self,event):
        self.textPad.event_generate('<<Copy>>')
    def  paste(self,event):
        self.textPad.event_generate('<<Paste>>')
    def undo(self,event):
        self.textPad.event_generate('<<Undo>>')
    def redo(self,event):
        self.textPad.event_generate('<<Redo>>')
    def select(self):
        self.textPad.tag_add('sel','1.0','end')
    def insert(self):
        self.infobar = Label(self.textPad, text='Line: 1 | Column: 0')
        self.infobar.pack(expand=NO, fill=None, side=RIGHT, anchor='se')
        currline, curcolumn = self.textPad.index("insert").split('.')
        self.infobar.config(text='Line: %s | Column: %s' % (currline,
                                                       curcolumn))
        self.infobar.pack(expand=NO, fill=None, side=RIGHT,
                          anchor='se')
    def theme(self):
        val=self.radio.get()
        l=['white','#83406A','#202B4B','#5B8340','#4B4620','#ffffBB','#D1E7E0']
        self.textPad.configure(bg=l[val-1])
    def update(self,interval=100):
        try:
            currline, curcolumn = self.textPad.index("insert").split('.')
            self.infobar.config(text='Line: %s | Column: %s' % (currline,
                                                                curcolumn))
        except:
            self.insert()
        self.infobar.after(interval, self.show_info_bar)
    def show_info_bar(self,interval=100):
        val=self.show2.get()
        if val:
            self.update()
        elif not val:
            self.infobar.destroy()
    def frame(self):
        self.shortcutbar = Frame(self.win, height=25, bg='light sea green')
        # creating icon toolbar
        icons = ['new', 'open', 'save', 'cut', 'copy', 'paste',
                 'undo', 'redo', 'find', 'about']
        for i, icon in enumerate(icons):
            tbicon = PhotoImage(file='icons/' + icon + '.png')
            cmd = eval('self.'+icon)
            toolbar = Button(self.shortcutbar, image=tbicon, command=cmd)
            toolbar.image = tbicon
            toolbar.pack(side=LEFT)
        self.shortcutbar.pack(expand=NO, fill=X)
        self.label=Label(self.win,width=2,bg="Red")
        self.label.pack(fill="y",side=tk.LEFT,anchor=NW)
    def search_for(self,needle, cssnstv, textPad, t2, e):
        textPad.tag_remove('match', '1.0', END)
        count = 0
        if needle:
            pos = '1.0'
            while True:
                pos = textPad.search(needle, pos, nocase=cssnstv,
                                     stopindex=END)
                if not pos: break
                lastpos = '%s+%dc' % (pos, len(needle))
                textPad.tag_add('match', pos, lastpos)
                count += 1
                pos = lastpos
        textPad.tag_config('match', foreground='red',
                           background='yellow')
        e.focus_set()
        t2.title('%d matches found' % count)
    def do_highlight(self,interval=100):
        self.textPad.tag_remove('active_line','1.0',END)
        self.textPad.tag_add("active_line", "insert linestart", "insert lineend+1c")
        self.textPad.tag_configure("active_line", background="ivory2")
        self.textPad.after(interval, self.highlight)
    def undo_highlight(self):
        self.textPad.tag_remove('active_line','1.0',END)
    def highlight(self):
        self.val=self.show3.get()
        if self.val:
            self.do_highlight()
        else:
            self.undo_highlight()
    def close_search(self):
        self.textPad.tag_remove('match', '1.0', END)

        self.t2.destroy()
    def updates(self,interval=100):
        txt = ''
        endline, endcolumn = self.textPad.index('end').split('.')
        txt = '\n'.join(map(str, range(1, int(endline))))
        self.label.config(text=txt, anchor='nw')
        self.label.after(interval,self.update_line_number)
    def update_line_number(self,event=None):
        if self.show1.get():
            self.updates()
    def find(self,event):
        self.t2=Toplevel(self.win)
        self.t2.title("Find")
        self.t2.geometry('262x65+200+250')
        self.t2.wm_transient(self.win)
        Label(self.t2,text="Find All:").grid(column=0,row=0)
        self.string=tk.StringVar()
        self.e=Entry(self.t2,width=25,textvariable=self.string)
        self.e.grid(column=1,row=0)
        self.check=tk.IntVar()
        Button(self.t2,text="Find All",command=lambda:
        self.search_for(self.string.get(), self.check.get(), self.textPad, self.t2, self.e)).grid(column=2,row=0)
        Checkbutton(self.t2,text="Ignore Case",variable=self.check).grid(column=1,row=1,sticky=tk.W)
        self.t2.protocol('WM_DELETE_WINDOW', self.close_search)  #
    def scroll(self):
        self.textPad = Text(self.win,undo=True)
        self.textPad.pack(expand=YES, fill=BOTH)
        self.textPad.focus()
        self.scroll = Scrollbar(self.textPad)
        self.textPad.configure(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.textPad.yview)
        self.scroll.pack(side=RIGHT, fill=Y)
    def about(self):
        messagebox.showinfo("Python GUI","This pad is made by yash rajput")
    def help(self,event):
        messagebox.showinfo("Python GUI","This is a sample practice piece")
oop=GUI()
oop.win.mainloop()