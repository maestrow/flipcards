import tkinter as tk
from tkinter import Tk, ttk

class Main(ttk.Frame):
  def __init__(self, master=None, **kw):
    ttk.Frame.__init__(self, master, **kw)
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    self.quitButton = ttk.Button(self, text='Quit', command=self.quit)
    self.quitButton.grid()


class App:
  def __init__(self, root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    main = Main(root, padding="30 30 120 120", borderwidth=10, relief="sunken")
    main.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))


root = Tk()
App(root)
root.mainloop()
