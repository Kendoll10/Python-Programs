# More programs on the if-elif-else statement

print("This program checks for zoo discount and the entrance price is $120")

price = 120
times = int(input("How many times have you being to the zoo before?\n"))

if times == 3:
    price = 120 - 30
    print("Your total included discount will be $", price)
elif times == 4:
    price = 120 - 50
    print("Your total included discount will be $", price)
elif times == 5:
    price = 120 - 60
    print("Your total discount will be $", price)
elif times >= 6:
    price = 120 - 70
    print("Your total discount will be $", price)
else:
    print("Your total price is $", price, "and you are not eligible for a discount at this time")
