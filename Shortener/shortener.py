import tkinter as tk
from tkinter.constants import END, LEFT, WORD, X
import pyshorteners

def shortenLink():
    url = urlText.get("1.0", END)
    newlink = pyshorteners.Shortener().tinyurl.short(url.strip())
    link.set(newlink)

def copyLink():
    root.clipboard_clear()
    root.clipboard_append(link.get().strip())

root = tk.Tk()
root.title('Link Shortener')
root.geometry('400x160')
root.resizable(0, 0)
icon = tk.PhotoImage(file='UrlShortner/icon.png')
root.iconphoto(False, icon)

mainFrame = tk.Frame(root, height=450, width=200, bg='black')
mainFrame.pack(fill=X)

titleLabel = tk.Label(mainFrame, text='Enter yor url below.', fg='red', bg='black', bd=5)
titleLabel.pack()

urlText = tk.Text(root, height=2, width=45, bd=3, wrap=WORD)
urlText.pack(pady=10)

link = tk.StringVar()
updateLabel = tk.Label(root, textvariable=link, fg='red', bd=3)
updateLabel.pack()

linkShortner = tk.Button(root, text='Shorten Link', bd=2, activebackground='light green', command=shortenLink)
linkShortner.pack(side=LEFT, padx=60)

copyButton = tk.Button(root, text='Copy Link', bd=2, activebackground='light green', command=copyLink)
copyButton.pack(side=LEFT)

root.mainloop()