# Week 3 SWDV-630 Inheritance TimeKeeper Percival Peters TimeKeeper.py

from NameKeeper import *

class TimeKeeper(NameKeeper):
    def __init__(self, firstName, lastName, date, time):
        self.date = date
        self.time = time
        NameKeeper.__init__(self, firstName, lastName) #  Should be indented at the same level as the self variables
    
    def punchIn(self, x): # There should be a self argument here. Also, x is not declared within the function. We need to pass an x argument for this to work
        # attempting to simulate punching in by using return statement
        return "You have punched in at" + x + "time!"
        
        
