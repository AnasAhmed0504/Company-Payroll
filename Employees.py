"""
We need to represent a Company and its Payroll
"""


#Working people either VOLUNTARY or EMPLOYEES

#The minimal common between them is name and address information

#Any working person is paid money based on its type

#Each employee is paid in a specific day (varying from a person to another)
# ○ Employees could be hourly based or salaried based.
#     ■ Also a commision salaried employee takes extra money as the ratio of the sales he did

"""
Develop the classes (high-level)
○ Features for each class type you figure out
○ amount_to_pay property that returns the salary
"""

class StaffMember:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
class Employee(StaffMember):
    def __init__(self, name, address, day_to_pay):
        super().__init__(name, address)
        self.day_to_pay = day_to_pay


class HourlyBasedEmployee(Employee):
    def __init__(self, name, address, day_to_pay, total_hours, money_per_hour):
        super().__init__(name, address, day_to_pay)
        self.total_hours = total_hours
        self.money_per_hour = money_per_hour
    
    @property
    def salary(self):
        return self.total_hours * self.money_per_hour


class SalaryBasedEmployee(Employee):
    def __init__(self, name, address, day_to_pay, money_per_month):
        super().__init__(name, address, day_to_pay)
        self.money_per_month = money_per_month

    @property 
    def salary(self):
        return self.money_per_month



class Commision(SalaryBasedEmployee):
    def __init__(self, name, address, day_to_pay, money_per_month, commision_rate, total_sales):
        super().__init__(name, address, day_to_pay, money_per_month)
        self.commision_rate = commision_rate
        self.total_sales = total_sales
        self.money_per_month = money_per_month
    
    @property
    def salary(self):
        return  super().money_per_month + self.commision_rate * self.total_sales 
        


class Voluntary(StaffMember):
    def __init__(self, name, address, current_payment):
        super().__init__(name, address)
        self.current_payment = current_payment

    def money_to_pay(self):
        return self.current_payment 

