#
#Author: Adrian Martinez
#Description: Program accepts number of inputs and helps user trace where their money is going.
# Inputs are broken down to percentages of total income with visual representation of total
# expenditures. If the input income exceeds maximum tax bracket, this is noted at the end of the
# program output. If the total output of expenditures exceeds income, this is noted at the end
# of the program output
#

print('-----------------------------')
print('----- WHERE\'S THE MONEY -----')
print('-----------------------------')

annual_salary = input('What is your annual salary?\n')          # User input on monthly expenditures
if not annual_salary.isnumeric() or (int(annual_salary) <= 0):  # If input is not a positive integer
    print('Must enter positive integer for salary.')            # program exits with prompt to enter
    exit(0)                                                     # type of input
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

tax_percent = 0                                             #Tax bracket dependent on user income
if (annual_salary > 0) and (annual_salary <=15000):
    tax_percent = 10
elif (annual_salary > 15000) and (annual_salary <=75000):
    tax_percent = 20
elif (annual_salary > 75000) and (annual_salary <=200000):
    tax_percent = 25
elif annual_salary > 200000:
    tax_percent = 30

taxes = annual_salary * (tax_percent / 100)

if int(taxes) >= 50000:                                     #Taxes are capped at $50,000
    taxes = 50000
    tax_percent = (taxes / annual_salary) * 100

total_expense = monthly_housing + monthly_bills + monthly_food + annual_travel + taxes
extra = annual_salary - total_expense

bill_percent = (monthly_bills / annual_salary) * 100        #Percentages calculated against annual
housing_percent =(monthly_housing / annual_salary) * 100    # salary and kept as a float
food_percent = (monthly_food / annual_salary) * 100
travel_percent = (annual_travel / annual_salary) * 100
extra_percent = extra / annual_salary * 100

#Max percentage calculated to set bracketed title and ending lines. Lines match the longest
# hashed visual representation of percentages
longest_percentage = max(int(bill_percent), int(housing_percent), int(food_percent),
                         int(travel_percent), int(tax_percent), int(extra_percent))

print()
print('-' * (42 + longest_percentage))
print('See the financial breakdown below, based on a salary of $' + str(annual_salary))
print('-' * (42 + longest_percentage))
#numbers are formatted to line up the user inputs
print('| mortgage/rent | $',  format(monthly_housing, '10,.2f'), '|', format(housing_percent,
    '5.1f') + '% |', "#" * int(housing_percent))
print('|         bills | $',  format(monthly_bills, '10,.2f'), '|', format(bill_percent,
    '5.1f') + '% |', "#" * int(bill_percent ))
print('|          food | $',  format(monthly_food, '10,.2f'), '|', format(food_percent,
    '5.1f') + '% |', "#" * int(food_percent))
print('|        travel | $',  format(annual_travel, '10,.2f'), '|', format(travel_percent,
    '5.1f') + '% |', "#" * int(travel_percent))
print('|           tax | $',  format(taxes, '10,.2f'), '|', format(tax_percent,
    '5.1f') + '% |', "#" * int(tax_percent))
print('|         extra | $',  format(extra, '10,.2f'), '|', format(extra_percent,
    '5.1f') + '% |', "#" * int(extra_percent))

print('-' * (42 + longest_percentage))

if extra < 0:                                   #If user inputs numbers that create either a
    print('>>> WARNING: DEFICIT <<<')           # deficit or reach the tax limit, it is noted
if taxes >= 50000:                              # here at the end of the program output.
    print('>>> TAX LIMIT REACHED <<<')