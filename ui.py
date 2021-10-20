import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from facebook import Facebook

def openFile():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    file = fd.askopenfile(
        mode="r",
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)
    content = file.read()
    file.close()
    return content


class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1341
        height=827
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_335=tk.Button(root)
        GButton_335["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_335["font"] = ft
        GButton_335["fg"] = "#000000"
        GButton_335["justify"] = "center"
        GButton_335["text"] = "Start"
        GButton_335.place(x=10,y=770,width=106,height=30)
        GButton_335["command"] = self.GButton_335_command

        GLineEdit_863=tk.Entry(root)
        GLineEdit_863["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_863["font"] = ft
        GLineEdit_863["fg"] = "#333333"
        GLineEdit_863["justify"] = "left"
        GLineEdit_863["text"] = "Page"
        GLineEdit_863.place(x=10,y=690,width=618,height=30)

        GButton_428=tk.Button(root)
        GButton_428["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_428["font"] = ft
        GButton_428["fg"] = "#000000"
        GButton_428["justify"] = "center"
        GButton_428["text"] = "..."
        GButton_428.place(x=630,y=690,width=30,height=30)
        GButton_428["command"] = self.GButton_428_command

        GLineEdit_62=tk.Entry(root)
        GLineEdit_62["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_62["font"] = ft
        GLineEdit_62["fg"] = "#333333"
        GLineEdit_62["justify"] = "left"
        GLineEdit_62["text"] = "Content"
        GLineEdit_62.place(x=10,y=730,width=619,height=30)

        GButton_294=tk.Button(root)
        GButton_294["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_294["font"] = ft
        GButton_294["fg"] = "#000000"
        GButton_294["justify"] = "center"
        GButton_294["text"] = "..."
        GButton_294.place(x=630,y=730,width=30,height=30)
        GButton_294["command"] = self.GButton_294_command

        GListBox_679=tk.Listbox(root)
        GListBox_679["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_679["font"] = ft
        GListBox_679["fg"] = "#333333"
        GListBox_679["justify"] = "center"
        GListBox_679.place(x=10,y=20,width=650,height=651)

        GListBox_342=tk.Listbox(root)
        GListBox_342["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_342["font"] = ft
        GListBox_342["fg"] = "#333333"
        GListBox_342["justify"] = "center"
        GListBox_342.place(x=680,y=20,width=650,height=652)

        self.facebook = Facebook()

    def GButton_335_command(self):
        print("start")

        print(self.pages) 

        self.facebook.reviews(self.pages, "test")

    def GButton_428_command(self):
        print("file 1")

        self.pages = openFile()
        print(self.pages)

        # showinfo(
        #     title='Selected File',
        #     message=openFile()
        # )


    def GButton_294_command(self):
        print("file 2")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()



