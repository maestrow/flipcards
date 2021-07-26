from django.core.management.base import BaseCommand
from fcards import models
import curses

class Command(BaseCommand):

  def doStuff():
    print("Hello, world")
    card = models.Card(foreign="aaaa", meaning="bbb")
    card.save()

    first_card = models.Card.objects.all()[-1]

    print(first_card.foreign)
    print(first_card.meaning)

  def window(self):
    screen = curses.initscr()
    for i in range(100):
      screen.addstr('ojf oweifjo wiejf owiej foi, {}\n'.format(i))
      screen.getch()
    curses.endwin()

  def handle(self, *args, **kwargs):
    curses.wrapper(self.window())



