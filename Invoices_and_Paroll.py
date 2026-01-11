# there are INVOICES
# each INVOICE has a set of ITEMS
# each ITEM has description, total quantity and price per item
# Each item has its own details (e.g. book author name)
# Invoice price: sum of the items’ prices

"""
The payroll consists of a payables list
○ Each payable is either employee or invoice
○ The total paid money is the total paid money for the added employees and invoices
"""

'''
Create class Company
○ It creates several types of payables, add to Payroll and compute total paid money
'''
from Employees import *


class Item():
    def __init__(self, description, total_quantity, price_per_item):
        super().__init__()
        self.description = description
        self.total_quantity = total_quantity
        self.price_per_price = price_per_item
    
    def cost(self):
        return self.total_quantity * self.price_per_price


class Book(Item):
    def __init__(self, description, total_quantity, price_per_item, author_name):
        super().__init__(description, total_quantity, price_per_item)
        self.author_name = author_name

class Electronic(Item):
    def __init__(self, description, total_quantity, price_per_item, warranty_years):
        super().__init__(description, total_quantity, price_per_item)
        self.warranty_years = warranty_years




class Invoices():
    def __init__(self, invoice_id):
        self.invoice_id = invoice_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    @property
    def amount_to_pay(self):
        return sum([item.price for item in self.items])



class Payroll():
    def __init__(self):
        self.payables = []
    
    def add_payable(self, payable):
        self.payables.append(payable)

    @property
    def total_paid_money(self):
        return sum([payable.amount_to_pay for payable in self.payables])
    


class Company:
    def __init__(self):
        self.payroll = Payroll()
    
    def run(self):
        self.payroll.add_payable(SalaryBasedEmployee("Alice", "123 Main St", 30, 3000))
        self.payroll.add_payable(HourlyBasedEmployee("Bob", "456 Elm St", 15, 160, 20))
        self.payroll.add_payable(Commision("Charlie", "789 Oak St", 25, 2000, 0.1, 5000))
        self.payroll.add_payable(Voluntary("David", "321 Pine St", 0))
    
        invoice = Invoices(1234)
        self.invoice.add_item(Book("Python Programming", 2, 50, "John Doe"))
        self.invoice.add_item(Electronic("Laptop", 1, 1000, 2))
        self.payroll.add_payable(invoice)

        print(self.payroll.total_paid_money)



if __name__ == '__main__':
    company = Company()
    company.fill_data(True)     # Try with True

    print(company.payroll.amount_to_pay)  
    