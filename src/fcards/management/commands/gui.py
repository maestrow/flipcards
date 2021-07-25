from django.core.management.base import BaseCommand
from fcards import models
import tkinter as tk
from tkinter import Tk, ttk


class Main(ttk.Frame):
  def __init__(self, master=None, **kw):
    ttk.Frame.__init__(self, master, **kw)

    # Init vars:
    self.lastGrade = tk.StringVar(value='...')
    self.front = tk.StringVar()
    self.back = tk.StringVar()
    self.notes = tk.StringVar()
    self.backVisible = False

    self.cards = models.Card.objects.all().order_by('pk')
    self.index = 0

    self.showCard()

    # Widgets:
    self.grid()
    self.createWidgets()
    self.columnconfigure(1, weight=1)
    self.rowconfigure(2, weight=1)

  # Actions

  def showCard(self):
    card = self.cards[self.index]
    self.front.set(card.meaning)
    self.back.set(card.foreign)
    self.notes.set(card.context)

  def rate(self, grade):
    card = self.cards[self.index]
    ratings = {
      0: 'Incorrect response',
      1: 'Correct response, after some hesitation',
      2: 'Perfect recall'
    }
    self.lastGrade.set(ratings[grade])
    self.wordsList.insert(0, '{} - {}'.format(card.meaning, card.foreign))

    self.index += 1
    self.hideBack()
    self.showCard()

  def showBack(self):
    self.lblBack.grid()
    self.lblNotes.grid()
    self.backVisible = True

  def hideBack(self):
    self.lblBack.grid_remove()
    self.lblNotes.grid_remove()
    self.backVisible = False

  def switchBack(self):
    if self.backVisible:
      self.hideBack()
    else:
      self.showBack()

  # Widgets

  def card(self, container):
    s = ttk.Style()
    s.configure('Card.TFrame', background='#BBBBBB')   # add background='black' to see frame area

    frame = ttk.Frame(container, style='Card.TFrame')
    self.lblFront = ttk.Label(frame, textvariable=self.front)
    self.lblFront.grid(column=1, row=1)
    self.lblBack = ttk.Label(frame, textvariable=self.back)
    self.lblBack.grid(column=1, row=2)
    self.lblNotes = ttk.Label(frame, textvariable=self.notes, wraplength=600)
    self.lblNotes.grid(column=1, row=3)

    self.hideBack()

    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=3)
    return frame

  def cardControl(self, container):
    frame = ttk.Frame(container, padding=30)
    self.card(frame).grid(column=1, row=1, columnspan=3, sticky='nwes')
    self.rateBad = ttk.Button(frame, text="bad", command=lambda *args: self.rate(0))
    self.rateBad.grid(row=2, column=1)
    self.rateGood = ttk.Button(frame, text="good", command=lambda *args: self.rate(1))
    self.rateGood.grid(row=2, column=2)
    self.rateExcelent = ttk.Button(frame, text="excelent", command=lambda *args: self.rate(2))
    self.rateExcelent.grid(row=2, column=3)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.rowconfigure(1, weight=1)
    return frame

  def stats(self, container):
    frame = ttk.Frame(container, padding=10)
    ttk.Label(frame, textvariable=self.lastGrade).grid()
    # frame.columnconfigure(0, weight=1)
    # frame.rowconfigure(0, weight=1)
    return frame

  def left(self, container):
    frame = ttk.Labelframe(container, text='Pane1', width=300, height=200, borderwidth=1, relief="ridge")
    self.cardControl(frame).grid(column=1, row=1, sticky='nwes')
    self.stats(frame).grid(column=1, row=2, sticky='nwes')
    # ttk.Label(frame, text="left").grid()
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(1, weight=1)
    return frame

  def right(self, container):
    frame = ttk.Labelframe(container, text='Pane2', width=300, height=200, borderwidth=1, relief="ridge")
    self.wordsList = tk.Listbox(frame, height=5)
    self.wordsList.grid(column=0, row=0, sticky='nwes')
    s = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.wordsList.yview)
    s.grid(column=1, row=0, sticky='ns')
    self.wordsList['yscrollcommand'] = s.set
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    # for i in range(1, 101):
    #   self.wordsList.insert('end', 'Line %d of 100' % i)

    return frame

  def createWidgets(self):
    self.header = ttk.Label(self, text='Header').grid(column=1, row=1)

    s = ttk.Style()
    s.configure('App.TPanedwindow.Vertical.Sash', sashthickness=5)

    self.main = ttk.PanedWindow(self, orient=tk.HORIZONTAL, style='App.TPanedwindow')
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
    self.main = Main(root, padding="30 30 30 30", borderwidth=10, relief="sunken")
    self.main.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))


class Command(BaseCommand):

  def openGui(self):
    root = Tk()
    root.title("Flip Cards")
    root.geometry('1000x600')
    app = App(root)
    root.bind("1", lambda *args: app.main.rateBad.invoke())
    root.bind("2", lambda *args: app.main.rateGood.invoke())
    root.bind("3", lambda *args: app.main.rateExcelent.invoke())
    root.bind("0", lambda *args: app.main.switchBack())
    root.mainloop()

  def handle(self, *args, **kwargs):
    self.openGui()