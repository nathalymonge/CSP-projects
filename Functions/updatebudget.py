def inp(type):
    insert = input(f"What is your monthly {type}: ")
    
    return int(insert)

def percent(type,amount):
    per = amount/income *100

    return(f"Your {type} is {per}% of income.")

print("Hello, and welcome to your financial calculator!\n")
income = inp("income")
rent = inp("rent")
utilities = inp("utilities")
groceries = inp("groceries")
transportation = inp("transportation")
savings = income *.2
expenses = rent + utilities + groceries + transportation
spend = income - savings - expenses
total = income - savings - expenses
print("Your monthly income is $",income)
print("Your monthly expenses are $",expenses)
print("Your monthly savings are $",savings)
print("You have $",total, "left to spend")

print(percent("rent", rent))
print(percent("utilities", utilities))
print(percent("groceries", groceries))
print(percent("transportation", transportation))
print(percent("savings", savings))
print(percent("expenses", expenses))