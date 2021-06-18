from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Text editor v1')
root.geometry("1200x660")

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def browseFiles():
   file_name = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
                                          
                                                                                                                                             
   file_name = open(file_name, 'r')
   stuff = file_name.read()
   input_txt.insert(END, stuff)
   file_name.close()

def Take_input():
   INPUT = inputtxt.get("1.0", "end-1c")
   print(INPUT)

def new_file():
   input_txt.delete("1.0", END)

    
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=browseFiles)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)


input_txt = Text(root, height = 100,
                width = 250,
                bg = "light yellow", font =("unisans", 13))
input_txt.pack()


root.config(menu=menubar)
root.mainloop()
