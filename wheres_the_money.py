#
#Author: Adrian Martinez
#Description: Program accepts number of inputs and helps user trace where their money is going
#

print('-----------------------------')
print('----- WHERE\'S THE MONEY -----')
print('-----------------------------')
annual_salary = input('What is your annual salary?\n')
if not annual_salary.isnumeric() or (int(annual_salary) <= 0):
    print('Must enter positive integer for salary.')
    exit(0)
else:
    annual_salary = int(annual_salary)

monthly_housing = input('How much is your monthly mortgage or rent?\n')
if not monthly_housing.isnumeric() or (int(monthly_housing) <= 0):
    print('Must enter positive integer for mortgage or rent.')
    exit(0)
else:
    monthly_housing = int(monthly_housing) * 12

monthly_bills = input('What do you spend on bills monthly?\n')
if not monthly_bills.isnumeric() or (int(monthly_bills) <= 0):
    print('Must enter positive integer for bills.')
    exit(0)
else:
    monthly_bills = int(monthly_bills) * 12

monthly_food = input('What are your weekly grocery/food expenses?\n')
if not monthly_food.isnumeric() or (int(monthly_food) <= 0):
    print('Must enter positive integer for food.')
    exit(0)
else:
    monthly_food = int(monthly_food) * 52

annual_travel = input('How much do you spend on travel annually?\n')
if not annual_travel.isnumeric() or (int(annual_travel) <= 0):
    print('Must enter positive integer for travel.')
    exit(0)
else:
    annual_travel = int(annual_travel)

tax_percent = 0
if (annual_salary > 0) and (annual_salary <=15000):
    tax_percent = 10
elif (annual_salary > 15000) and (annual_salary <=75000):
    tax_percent = 20
elif (annual_salary > 75000) and (annual_salary <=200000):
    tax_percent = 25
elif annual_salary > 200000:
    tax_percent = 30
taxes = annual_salary * (tax_percent / 100)
tax_percent = float(format(tax_percent, '.1f'))


total_expense = monthly_housing + monthly_bills + monthly_food + annual_travel
extra = annual_salary - (monthly_housing + monthly_bills + monthly_food + annual_travel)
bill_percent = monthly_bills / total_expense
housing_percent = monthly_housing / total_expense
food_percent = monthly_food / total_expense
travel_percent = annual_travel / total_expense
extra_percent = extra / (total_expense + annual_salary)

print()
print('--------------------------')
print('See the financial breakdown below, based on a a salary of $', annual_salary)
print('----------------------------------------------' )

print('| mortgage/rent | $',  format(monthly_housing, '11,.2f'), '|',
      format(housing_percent, '6.1%'), "|", "#" * int(housing_percent * 10))
print('|         bills | $',  format(monthly_bills, '11,.2f'), '|',
      format(bill_percent, '6.1%'), "|", "#" * (int(bill_percent * 10)))
print('|          food | $',  format(monthly_food, '11,.2f'), '|',
      format(food_percent, '6.1%'), "|", "#" * (int(food_percent * 10)))
print('|        travel | $',  format(annual_travel, '11,.2f'), '|',
      format(travel_percent, '6.1%'), "|", "#" * (int(housing_percent * 10)))
print('|           tax | $',  format(taxes, '11,.2f'), '|', tax_percent, "|", "#" * (int(tax_percent)))
print('|         extra | $',  format(extra, '11,.2f'), '|',
      format(extra_percent, '6.1%'), "|", "#" * (int(extra_percent * 10)))

print('---------------------------------------------------------------------')

if extra < 0:
    print('>>>> WARNING: DEFICIT <<<<')
if taxes >= 50000:
    print('>>>> TAX LIMIT REACHED <<<<')
#| mortgge/rent | $  24,000.00 |  60.0% |
