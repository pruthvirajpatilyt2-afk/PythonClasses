from tkinter import *
from appdata.coredata import data
class screen(Tk):
    def __init__(self):
        super().__init__()
        self.appdata = data()
        self.title(self.appdata.app_title)
        self.size=self.appdata.LoadingSize
        self.geometry(self.size)
        loadingtitle=Label(self, text=self.appdata.name, foreground='#472ADE')
        loadingtitle.pack()

    def content(self):
        pass
    def show(self):
        self.resizable(False, False)
        self.mainloop()

if __name__=='__main__':
    screen().show()