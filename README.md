# Company-Payroll
### The goal of this project is high-level design NOT full-implementation

○ There is no menu of options. No deep details. Goal is design

○ Also another goal is to deal with requirements that might seems vague

### Employees
We need to represent a Company and its Payroll

Working people either VOLUNTARY or EMPLOYEES

The minimal common between them is name and address information

Any working person is paid money based on its type

Each employee is paid in a specific day (varying from a person to another)
 
Employees could be hourly based or salaried based.

Also a commision salaried employee takes extra money as the ratio of the sales he did


Develop the classes (high-level)

 Features for each class type you figure out

 amount_to_pay property that returns the salary

 ### Invoices & Payroll
 there are INVOICES

each INVOICE has a set of ITEMS

each ITEM has description, total quantity and price per item

Each item has its own details (e.g. book author name)

Invoice price: sum of the items’ prices

The payroll consists of a payables list

 Each payable is either employee or invoice

 The total paid money is the total paid money for the added employees and invoices

Create class Company

 It creates several types of payables, add to Payroll and compute total paid money

### Validations
Background: In practice, we may need to verify invoices.

○ E.g. an invoice is out-of-date relative to some deals with suppliers

○ E.g. the computed taxes doesn't utilize some advantages in the country

We can create several validation rules, one for every purpose

 In future, more rules might be added

 You don't need to care about the validation rules logic


A Validator Group consists of a subset of the available validation rules

 E.g. Mandatory-Validator has a very few validation rules to be fast in evaluation

 E.g. Complete-Validator has all the validation rules coded so far

 In short: the validator just make sure all its rules are valid

 Before paying for an invoice, it must pass all validation rules in its validator group

### Payroll Printing
We would like to be able to print the payroll content (repr), however we would
like them to be ordered


**Ordering Criteria**

 If the object type is not the same (e.g.invoice vs HourlyEmployee / SalariedEmployee vs

CommissionSalariedEmployee) ⇒ Compare based on class name string

 If they are the same:
 
 If it is a working person, then compare based on name then salary (increasing)
 
 If it is an invoice: then compare based on invoice ID, then # of items in an invoice

**Printing**

 Employee ⇒ Class name, Employee Name, Employee Address

 Invoice ⇒ Class name, ID, # of items
