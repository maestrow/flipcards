import tkinter as tk
from tkinter import Tk, ttk


class Main(ttk.Frame):
  def __init__(self, master=None, **kw):
    ttk.Frame.__init__(self, master, **kw)
    self.grid()
    self.createWidgets()
    self.columnconfigure(1, weight=1)
    self.rowconfigure(2, weight=1)

  def left(self, container):
    frame = ttk.Labelframe(container, text='Pane1', width=300, height=200, borderwidth=10, relief="sunken")
    ttk.Label(frame, text="left").grid()
    return frame

  def right(self, container):
    frame = ttk.Labelframe(container, text='Pane2', width=300, height=200, borderwidth=10, relief="sunken")
    ttk.Label(frame, text="right").grid()
    return frame

  def createWidgets(self):
    self.header = ttk.Label(self, text='Header').grid(column=1, row=1)

    s = ttk.Style()
    s.configure('My.TPanedwindow.Vertical.Sash', sashthickness=100, sashrelief='sunken')

    self.main = ttk.PanedWindow(self, orient=tk.HORIZONTAL, style='My.TPanedwindow')
    self.main.grid(column=1, row=2, sticky=(tk.N, tk.W, tk.E, tk.S))
    left = self.left(self.main)
    right = self.right(self.main)
    self.main.add(left, weight=1)
    self.main.add(right, weight=0)

    self.footer = ttk.Label(self, text="status bar").grid(column=1, row=3)


class App:
  def __init__(self, root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    main = Main(root, padding="30 30 30 30", borderwidth=10, relief="sunken")
    main.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))


root = Tk()
root.title("Flip Cards")
App(root)
root.mainloop()
