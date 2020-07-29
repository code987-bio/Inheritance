# Week 3 SWDV-630 Inheritance Main Percival Peters.py

from NameKeeper import *
from TimeKeeper import *

class TimeKeeper2(NameKeeper):
    def __init__(self, firstName, lastName, date, time):
        self.date = date
        self.time = time

def punchOut():
        # attempting to simulate punching out by using return statement
        return "You have punched out at" + x + "time!" 


