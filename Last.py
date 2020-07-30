# Week 3 SWDV-630 Inheritance Last Percival Peters.py

from NameKeeper import *
from TimeKeeper import *
from Main import *

class TimeKeeper3(NameKeeper):
    def __init__(self, firstName, lastName, date, time):
        self.date = date
        self.time = time
        
    def showPunchOutTime():
        x = datetime.datetime.now()
        print(x)
    
    p1 = Employee("John", "Doe")  # There is no class employee. Therefore, this won't compile when you will run your code. Replace with Namekeeper?
    print(p1.firstName, p1.lastName)
    
    
 # ------------------------
 
    def Main():
        employeePunchIn = Timekeeper("John", "Doe", "11/21/2011", "06:30am")
        employeePunchOut = Timekeeper2("John", "Doe", "11/21/2011", "10:30am")
         
   
    
# Declaration
    def testMethod(employeePunchIn, employeePunchOut):
        print("John Doe has clocked in at 06:30am on 11/21/2011")
        print("John Doe has clocked out at 10:30am on 11/21/2011")

testMethod():  # To test these, you should create an object of a class first. 
print("name keeper attribute 1", NameKeeper.firstName)  # All these items should be indented
print("name keeper attribute 2", NameKeeper.lastName)
print("time keeper attribute 1", TimeKeeper.firstName)
print("time keeper attribute 2", TimeKeeper.lastName)
print("time keeper attribute 3", TimeKeeper.date)
print("time keeper attribute 4", TimeKeeper.time)
print("time keeper 2 attribute 1", TimeKeeper2.firstName)
print("time keeper 2 attribute 2", TimeKeeper2.lastName)
print("time keeper 2 attribute 3", TimeKeeper2.date)
print("time keeper 2 attribute 4", TimeKeeper2.time)    
print("time keeper 3 attribute 1", TimeKeeper3.firstName)
print("time keeper 3 attribute 2", TimeKeeper3.lastName)
print("time keeper 3 attribute 3", TimeKeeper3.date)
print("time keeper 3 attribute 4", TimeKeeper3.time)
print("time keeper method 1", TimeKeeper.punchIn)
print("name keeper method 1", NameKeeper.showEmployeeId)
print("name keeper method 2", NameKeeper.showTodaysDate)
print("time keeper 2 method 1", TimeKeeper2.punchOut)
print("time keeper 3 method 1", TimeKeeper3.showPunchOutTime)
print("time keeper 3 method 2", TimeKeeper3.Main)

# Class invocation
Main()  # To create a class invocation, you should create an object of that class (e.g. p1 = Timekeeper3("Joe", "Doe", date, time)
    
#method call
testMethod(employeePunchIn, employeePunchOut) # Should be moved outside of class. An object should be created first
