# Using if, elif and else statement in a python program

print("This program checks if you are eligible for a bank loan or not")

salary = int(input("How much is your salary\n"))

if salary > 1000:
    amount = 200
    print("You are eligible of obtaining a bank loan by paying $", amount, "monthly")
elif salary == 1000:
    amount = 500
    print("You are eligibel to get a bank loan with a higher monthly price of $", amount)
else:
    print("You are not eligible to obtain a bank loan")