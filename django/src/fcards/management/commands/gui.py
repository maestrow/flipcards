from django.core.management.base import BaseCommand
from django.db.models import Q, Expression, F, DateTimeField, ExpressionWrapper, Value
from django.db.models.functions import Now
from django.db.models.expressions import RawSQL
from fcards import models
import tkinter as tk
from tkinter import Tk, ttk, messagebox
from datetime import datetime
import argparse

def getCardsQuery():
    query = models.Card.objects.annotate(learn_time=RawSQL("last_review + interval '1 day' * i", []))
    # query = query.filter(learn_time__lte=Now())
    query = query.filter(deck__id__in=[130])
    query = query.order_by('learn_time', 'pk')[:500]
    return query

class Main(ttk.Frame):
  def __init__(self, master, options, **kw):
    ttk.Frame.__init__(self, master, **kw)

    # Init vars:
    self.lastGrade = tk.StringVar(value='...')
    self.front = tk.StringVar()
    self.back = tk.StringVar()
    self.notes = tk.StringVar()
    self.backVisible = False

    self.cards = getCardsQuery()
    self.index = 0
    self.showCurrentCard()

    # Widgets:
    self.grid()
    self.createWidgets()
    self.columnconfigure(1, weight=1)
    self.rowconfigure(2, weight=1)

    if options['learn']:
      for c in self.cards:
        self.wordsList.insert(0, '{} - {}'.format(c.meaning, c.foreign))
      self.index = self.cards.count() - 1  # ToDo: Ugly hack
      self.showCurrentCard()
      self.index = self.cards.count()

  # === Helpers

  def currentCard(self):
    return self.cards[self.index]

  # === Actions

  def showCard(self, card):
    self.front.set(card.meaning)
    self.back.set(card.foreign)
    self.notes.set(card.context)

  def showCurrentCard(self):
    card = self.currentCard()
    self.showCard(card)

  def showNextCard(self):
    self.index += 1
    self.hideBack()
    self.showCurrentCard()

  def showSelectedHistoryCard(self):
    selection = self.wordsList.curselection()
    if selection:
      index = selection[0]
      card = self.cards[self.index - index - 1]
      self.showCard(card)

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

  def setStateForRateActions(self, state):
    self.btnRateBad.state(state)
    self.btnRateGood.state(state)
    self.btnRateExcelent.state(state)

  def updateCardState(self, card: models.Card, grade: int):
    if grade > 0:
      if card.n == 0:
        card.i = 1
      elif card.n == 1:
        card.i = 3
      else:
        card.i = round(card.i * card.ef)
      card.ef = card.ef + (0.1 - (2 - grade) * (0.08 + (2 - grade) * 0.02))
      if card.ef < 1.3:
        card.ef = 1.3
      card.n += 1
    else:
      card.n = 0
      card.i = 1
    card.last_review = datetime.now()
    card.save()

  # === Event Handlers, Callbacks

  def onRate(self, grade):
    if self.wordsList.curselection() or self.index >= self.cards.count():
      return

    card = self.currentCard()
    ratings = {
      0: 'Incorrect response',
      1: 'Correct response, after some hesitation',
      2: 'Perfect recall'
    }
    self.lastGrade.set(ratings[grade])
    self.wordsList.insert(0, '{} - {}'.format(card.meaning, card.foreign))
    self.updateCardState(card, grade)

    if self.index >= self.cards.count() - 1:
      messagebox.showinfo(message='You have done all {} cards'.format(self.cards.count()))
      self.index += 1
    else:
      self.showNextCard()

  def onWordsListSelect(self, event):
    self.setStateForRateActions(["disabled"])
    self.btnContinue.state(["!disabled"])
    self.showBack()
    self.showSelectedHistoryCard()

  def onContinueClick(self, *args):
    self.setStateForRateActions(["!disabled"])
    self.btnContinue.state(["disabled"])
    self.wordsList.selection_clear(0, tk.END)
    self.hideBack()
    self.showCurrentCard()

  # === Widgets

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
    self.btnRateBad = ttk.Button(frame, text="(1) Bad", command=lambda *args: self.onRate(0))
    self.btnRateBad.grid(row=2, column=1)
    self.btnRateGood = ttk.Button(frame, text="(2) Good", command=lambda *args: self.onRate(1))
    self.btnRateGood.grid(row=2, column=2)
    self.btnRateExcelent = ttk.Button(frame, text="(3) Excellent", command=lambda *args: self.onRate(2))
    self.btnRateExcelent.grid(row=2, column=3)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.rowconfigure(1, weight=1)
    return frame

  def stats(self, container):
    frame = ttk.Frame(container, padding=10)
    ttk.Label(frame, textvariable=self.lastGrade).grid()
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    return frame

  def left(self, container):
    frame = ttk.Labelframe(container, text='Card', width=300, height=200, borderwidth=1, relief="ridge")
    self.cardControl(frame).grid(column=1, row=1, sticky='nwes')
    self.stats(frame).grid(column=1, row=2, sticky='nwes')
    # ttk.Label(frame, text="left").grid()
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(1, weight=1)
    return frame

  def right(self, container):
    frame = ttk.Labelframe(container, text='History', width=300, height=200, borderwidth=1, relief="ridge")
    self.wordsList = tk.Listbox(frame, height=5)
    self.wordsList.bind("<<ListboxSelect>>", self.onWordsListSelect)
    self.wordsList.grid(column=0, row=0, sticky='nwes')
    self.btnContinue = ttk.Button(frame, text="Continue", command=self.onContinueClick, state=["disabled"])
    self.btnContinue.grid(column=0, row=2, rowspan=2)
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
  def __init__(self, root, options):
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    self.main = Main(root, options, padding="30 30 30 30", borderwidth=10, relief="sunken")
    self.main.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

class Command(BaseCommand):

  def openGui(self):
    root = Tk()
    root.title("Flip Cards")
    root.geometry('1000x600')
    app = App(root, self.options)
    root.bind("1", lambda *args: app.main.btnRateBad.invoke())
    root.bind("2", lambda *args: app.main.btnRateGood.invoke())
    root.bind("3", lambda *args: app.main.btnRateExcelent.invoke())
    root.bind("0", lambda *args: app.main.switchBack())
    root.mainloop()

  def add_arguments(self, parser):
    parser.add_argument('--learn', action='store_true')

  def handle(self, *args, **options):
    self.options = options
    self.openGui()
