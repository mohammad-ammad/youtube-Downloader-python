from pytube import YouTube as yt
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
import threading
#04BEF3
file_name = ""
class Main(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x450")
        self.title("OurDownloader")
        self.iconbitmap("youtube.ico")
        self.config(bg="#0F5589")
        global url, n, choices, btn2
        self.columnconfigure(0, weight=1)
        l1 = Label(self, text="Youtube Video Downloader", width=50, font="comicsms 15 bold", fg="white", bg="#0F5589", pady=30)
        l1.grid()
        l2 = Label(self, text="Paste URL here:", width=30, font="comicsms 10", fg="white", bg="#0F5589")
        l2.grid()
        url = StringVar()
        urlEntry = Entry(self, textvariable=url, width=50)
        urlEntry.grid()
        l3 = Label(self, text="Choose File Path:", width=30, font="comicsms 10", fg="white", bg="#0F5589", pady=30)
        l3.grid()
        btn1 = Button(self, text="Choose File", font="comicsms 10 bold", fg="white", bg="#04BEF3", activebackground="#0F5589",
                      command=self.getfilepath)
        btn1.grid()
        l4 = Label(self, text="Choose Quality:", width=30, font="comicsms 10", fg="white", bg="#0F5589", pady=30)
        l4.grid()
        choices = ['720', '144', 'audio only']
        n = StringVar()
        combo = Combobox(self, width=20, textvariable=n, values=choices)
        combo.grid()
        btn2 = Button(self, text="Download", font="comicsms 10 bold", fg="white", bg="#04BEF3",
                      activebackground="#0F5589", width=30, command=self.geturl)
        btn2.place(x=50,y=400)

    def geturl(self):
        var = threading.Thread(target=self.downloading())
        var.start()

    def getfilepath(self):
        global file_name
        file_name = filedialog.askdirectory()

    def downloading(self):
        global select
        var = url.get()
        choice = n.get()
        video = yt(var, on_progress_callback=self.progress_func)
        if choice == choices[0]:
            select = video.streams.filter(progressive=True).first()
        elif choice == choices[1]:
            select = video.streams.filter(progressive=True).last()
        elif choice == choices[2]:
            select = video.streams.filter(only_audio=True).first()
        select.download(file_name)


if __name__ == '__main__':
    obj = Main()
    obj.mainloop()

