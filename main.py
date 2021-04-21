from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from tkinter.colorchooser import askcolor
import datetime
import webbrowser
from tkinter.filedialog import askopenfilename, asksaveasfilename

def line():
    lin = "_" * 100
    text.insert(INSERT,lin)

def date():
    data = datetime.date.today()
    text.insert(INSERT,data)
    
def normal():
    text.config(font = ("Arial", 12))

def bold():
    text.config(font = ("Arial", 12, "bold"))

def underline():
    text.config(font = ("Arial", 12, "underline"))

def italic():
    text.config(font = ("Arial",12,"italic"))

def font():
    (triple,color) = askcolor()
    if color:
       text.config(foreground=color)
       
def kill():
    root.destroy()

def opn():
    text.delete(1.0 , END)
    file = open(askopenfilename() , 'r')
    if file != '':
        txt = file.read()
        text.insert(INSERT,txt)
    else:
        pass
    
def save():
    filename = asksaveasfilename()
    if filename:
        alltext = text.get(1.0, END)                      
        open(filename, 'w').write(alltext)
        
def copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())
    
def paste():
    try:
        teext = text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT, teext)
    except:
        tkMessageBox.showerror("Error","The notes are empty!")

def clear():
    sel = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)
    
def clearall():
    text.delete(1.0 , END)

def background():
    (triple,color) = askcolor()
    if color:
       text.config(background=color)

def about():
    ab = Toplevel(root)
    ab.title("Jsplanetext - About")
    ab.iconbitmap('./jsplanetext.png')
    txt = "Jsplanetext™ \nBy Jscoderfly™\n Jscoderfly.github.io\nMIT License"
    la = Label(ab,text=txt,foreground='black')
    la.pack()
    ab.geometry("300x80")
    ab.resizable(0,0)

def web():
    webbrowser.open('https://Jscoderfly.github.io/')

def jscoderfly():
    webbrowser.open('https://github.com/Jscoderfly/')

root = Tk()
root.title("Jsplanetext - Open source text editor")
root.iconbitmap('./jsplanetext.png')
menu = Menu(root)

filemenu = Menu(root)
root.config(menu = menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=opn)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=kill)

editmenu = Menu(root)
menu.add_cascade(label="Edit",menu = editmenu)
editmenu.add_command(label="Copy", command = copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_separator()
editmenu.add_command(label = "Clear", command = clearall)

insmenu = Menu(root)
menu.add_cascade(label="Insert",menu= insmenu)
insmenu.add_command(label="Date",command=date)
insmenu.add_command(label="Line",command=line)
      
formatmenu = Menu(menu)
menu.add_cascade(label="Format",menu = formatmenu)
formatmenu.add_separator()
formatmenu.add_radiobutton(label='normal',command=normal)
formatmenu.add_radiobutton(label='bold',command=bold)
formatmenu.add_radiobutton(label='underline',command=underline)
formatmenu.add_radiobutton(label='italic',command=italic)

option_menu = Menu(root)
menu.add_cascade(label="Option",menu=option_menu)
option_menu.add_cascade(label="Text Color", command = font)
option_menu.add_command(label="Background Color", command=background)

helpmenu = Menu(menu)
menu.add_cascade(label="?", menu=helpmenu)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Website", command = web)
helpmenu.add_command(label="Jscoderfly", command = jscoderfly)
text = Text(root, height=1000, width=1000, font = ("Arial", 12))

scroll = Scrollbar(root, command=text.yview)
scroll.config(command=text.yview)                  
text.config(yscrollcommand=scroll.set)           
scroll.pack(side=RIGHT, fill=Y)
text.pack()
root.resizable(1,1)
root.geometry("1200x600")
root.mainloop()
