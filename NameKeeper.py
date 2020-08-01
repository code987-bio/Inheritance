import datetime

# Week 3 SWDV-630 Inheritance NameKeeper Percival Peters.py

class NameKeeper:
    def __init__(self, firstName, lastName):
       self.firstName = firstName
       self.lastName = lastName
       
    def showEmployeeId():
        # attempting to print employee id with the return statement
        employeeId = input("What is your employee ID?(Six numbers) ")
        return employeeId
    
    def showTodaysDate():
        x = datetime.datetime.now()
        print(x)
    
# Delete the call. To create a class, you should define it in your main file
