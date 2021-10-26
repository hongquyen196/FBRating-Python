import time
import os
import configparser
import random
import tkinter as tk
import tkinter.font as tkFont

from tkinter import filedialog as fd
from tkinter import messagebox
from facebook import Facebook

CONFIG = configparser.ConfigParser()
CONFIG.read("data.ini")


def storage_file(option, value=None):
    if not CONFIG.has_section('FILE'):
        CONFIG.add_section("FILE")

    CONFIG.set("FILE", option, value)


def open_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    file = fd.askopenfile(
        mode="r",
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)
    return file


class App:

    def __init__(self, root):
        self.root = root;
        # setting title
        root.title("Facebook automation tool")
        # setting window size
        width = 1341
        height = 827
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_335 = tk.Button(root)
        GButton_335["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_335["font"] = ft
        GButton_335["fg"] = "#000000"
        GButton_335["justify"] = "center"
        GButton_335["text"] = "Start"
        GButton_335.place(x=10, y=770, width=106, height=30)
        GButton_335["command"] = self.GButton_335_command

        GLineEdit_863 = tk.Entry(root)
        GLineEdit_863["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_863["font"] = ft
        GLineEdit_863["fg"] = "#333333"
        GLineEdit_863["justify"] = "left"
        GLineEdit_863["text"] = "Page"
        GLineEdit_863.place(x=10, y=690, width=618, height=30)

        GButton_428 = tk.Button(root)
        GButton_428["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_428["font"] = ft
        GButton_428["fg"] = "#000000"
        GButton_428["justify"] = "center"
        GButton_428["text"] = "..."
        GButton_428.place(x=630, y=690, width=30, height=30)
        GButton_428["command"] = self.GButton_428_command

        GLineEdit_62 = tk.Entry(root)
        GLineEdit_62["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_62["font"] = ft
        GLineEdit_62["fg"] = "#333333"
        GLineEdit_62["justify"] = "left"
        GLineEdit_62["text"] = "Content"
        GLineEdit_62.place(x=10, y=730, width=619, height=30)

        GButton_294 = tk.Button(root)
        GButton_294["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_294["font"] = ft
        GButton_294["fg"] = "#000000"
        GButton_294["justify"] = "center"
        GButton_294["text"] = "..."
        GButton_294.place(x=630, y=730, width=30, height=30)
        GButton_294["command"] = self.GButton_294_command

        GListBox_679 = tk.Listbox(root)
        GListBox_679["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_679["font"] = ft
        GListBox_679["fg"] = "#333333"
        GListBox_679["justify"] = "left"
        GListBox_679.place(x=10, y=20, width=650, height=651)

        GListBox_342 = tk.Listbox(root)
        GListBox_342["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_342["font"] = ft
        GListBox_342["fg"] = "#333333"
        GListBox_342["justify"] = "left"
        GListBox_342.place(x=680, y=20, width=650, height=652)

        GLabel_174=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_174["font"] = ft
        GLabel_174["fg"] = "#333333"
        GLabel_174["justify"] = "left"
        GLabel_174["text"] = "Message"
        GLabel_174.place(x=140,y=770,width=70,height=25)

        self.listbox_pages = GListBox_679
        self.listbox_contents = GListBox_342
        self.entry_pages = GLineEdit_863
        self.entry_contents = GLineEdit_62
        self.label_message = GLabel_174

    def entry_add(self, entry, value):
        entry.delete(0, "end")
        entry.insert(0, value)

    def listbox_add(self, listbox, values):
        listbox.delete(0, "end")
        for index, value in enumerate(values):
            listbox.insert(index+1, value)

    def GButton_335_command(self):
        print("start")
        
        # self.facebook = Facebook("/Users/qhle/Library/Application Support/Firefox/Profiles/vzc6qzxv.default-release")

        if (self.pages and self.contents):
            for index, page in enumerate(self.pages):
                self.listbox_pages.itemconfig(index, foreground='blue')
                try:
                    page = page.rstrip('\r\n').rstrip('/')
                    print("page: " + page)
                    self.label_message.configure(text=page)
                    content = random.choice(self.contents)
                    print("content: " + content)
                    split = content.split("|")
                    text = split[0].rstrip('\r\n')
                    photo = split[1].rstrip('\r\n')
                    # self.facebook.reviews_page(page, text, photo)
                except Exception as e:
                    print(str(e))

            messagebox.showinfo('Message', 'Reviews done.')

    def GButton_428_command(self):
        print("open pages file")

        file = open_file()

        self.entry_add(self.entry_pages, file.name)
        self.pages = file.readlines()
        self.listbox_add(self.listbox_pages, self.pages)

        storage_file("page", file.name)
        # print(self.pages)

        file.close()

    def GButton_294_command(self):
        print("open contents file")

        file = open_file()

        self.entry_add(self.entry_contents, file.name)
        self.contents = file.readlines()
        self.listbox_add(self.listbox_contents, self.contents)

        storage_file("content", file.name)
        # print(self.contents)

        file.close()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            try:
                # Write file after close app.
                with open('data.ini', 'w') as configfile:
                    CONFIG.write(configfile)

                # Close browser
                self.facebook.quit()
            except Exception as e:
                print(str(e))
            root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)

    if CONFIG.has_option("FILE", "page"):
        page = CONFIG.get("FILE", "page")
        app.entry_add(app.entry_pages, page)
        page_file = open(page)
        app.pages = page_file.readlines()
        app.listbox_add(app.listbox_pages,  app.pages)

    if CONFIG.has_option("FILE", "content"):
        content = CONFIG.get("FILE", "content")
        app.entry_add(app.entry_contents, content)
        content_file = open(content)
        app.contents = content_file.readlines()
        app.listbox_add(app.listbox_contents, app.contents)

    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
