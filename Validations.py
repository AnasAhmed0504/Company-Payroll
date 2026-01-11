"""
Background: In practice, we may need to verify invoices.
○ E.g. an invoice is out-of-date relative to some deals with suppliers
○ E.g. the computed taxes doesn't utilize some advantages in the country
"""

'''
We can create several validation rules, one for every purpose
○ In future, more rules might be added
○ You don't need to care about the validation rules logic
'''

"""
A Validator Group consists of a subset of the available validation rules
○ E.g. Mandatory-Validator has a very few validation rules to be fast in evaluation
○ E.g. Complete-Validator has all the validation rules coded so far
○ In short: the validator just make sure all its rules are valid
"""
# Before paying for an invoice, it must pass all validation rules in its validator group


from abc import ABC, abstractmethod



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
        


class Volunteer(StaffMember):
    def __init__(self, name, address, current_payment):
        super().__init__(name, address)
        self.current_payment = current_payment

    def money_to_pay(self):
        return self.current_payment 

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





class ValidationsRule(ABC):
    @abstractmethod
    def is_valid(self, invoice):
        pass

class TaxesValidationRule(ValidationsRule):
    def is_valid(self, invoice):
        print('Validating TaxesValidationRule')
        return True

class SuppliersDealsValidationRule(ValidationsRule):
    def is_valid(self, invoice):
        print('Validating SuppliersDealsValidationRule')
        return False


class InvoiceValidator:
    def __init__(self, rules):
        self.rules = rules
    
    def validate(self, invoice: ValidationsRule):
        if not self.rules:
            raise ValueError('Zero rules list.')
        
        for rule in self.rules:
            if not rule.is_valid(invoice):
                return False
        return True

class MandatoryInvoiceValidator(InvoiceValidator):
    @staticmethod
    def get_instance():
        rule = [TaxesValidationRule()]
        return MandatoryInvoiceValidator(rule)


class CompleteInvoiceValidator(InvoiceValidator):
    @staticmethod
    def get_instance():
        rule = [TaxesValidationRule(), SuppliersDealsValidationRule()]
        return CompleteInvoiceValidator(rule)
    
class ValidationError(BaseException):
    pass



class Invoices():
    def __init__(self, invoice_id, validator: InvoiceValidator):
        self.invoice_id = invoice_id
        self.validator = validator
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    @property
    def amount_to_pay(self):
        if not self.validator.validate(self):
            raise ValidationError('Invoice validation failed.')
        return sum([item.cost() for item in self.items])
    
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
    
    def fill_data(self, is_mandatory_validator = True):
        self.payroll.add_payable(SalaryBasedEmployee("Alice", "123 Main St", 30, 3000))
        self.payroll.add_payable(HourlyBasedEmployee("Bob", "456 Elm St", 15, 160, 20))
        self.payroll.add_payable(Commision("Charlie", "789 Oak St", 25, 2000, 0.1, 5000))
        self.payroll.add_payable(Volunteer("David", "321 Pine St", 0))
    
        if is_mandatory_validator:
            validator = MandatoryInvoiceValidator.get_instance()
        else:
            validator = CompleteInvoiceValidator.get_instance()
        invoice = Invoices(1234, validator)
        invoice.add_item(Book("Python Programming", 2, 50, "John Doe"))
        invoice.add_item(Electronic("Laptop", 1, 1000, 2))
        self.payroll.add_payable(invoice)
        