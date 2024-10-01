def inp(type):
    return int(input(f"What is your monthly{type}"))

print("Hello, and welcome to your financial calculator!\n")
income = int(input("What is your monthly income?: "))
rent = int(input("What is your monthly rent: "))
utilities = int(input("What is your monthly utilities: "))
groceries = int(input("What is your monthly groceries: "))
transportation = int(input("What does your monthly transportation cost: "))
expenses = rent + utilities + transportation + groceries
savings = income *.2
total = income - savings - expenses
print("Your monthly income is $",income)
print("Your monthly expenses are $",expenses)
print("Your monthly savings are $",savings)
print("You have $",total, "left to spend")


def percent(type,amount):
    per = amount/income *100

    return(f"Your {type} is {per}% of income.")

print(percent("rent", rent))
print(percent("utilities", utilities))
print(percent("groceries", groceries))
print(percent("transportation", transportation))
print(percent("savings", savings))
print(percent("expenses", expenses))