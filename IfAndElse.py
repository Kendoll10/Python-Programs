# Make sure to copy and run the codes separately on your editor to see the results

# using If and Else statement in python

var = 10

if var == 22:
    print("var is = 10")
else:
    print("var is NOT = 10")

# using >, <, >=, <=, == in an if and else statement

greater = 10
less = 5

if greater == less:          # you can change the signs and try them out on your text editor
    print("Yes")
else:
    print("No")


# Comparing strings using if statement in python

name = "Python"
name2 = "C++"

if name == name2:
    print("Two strings are equal")
else:
    print("Two strings are not equal")


# using not equal with if, else statement

num = 10
num2 = 15

if num != num2:
    print("Num is not equal to num2")
else:
    print("num is equal to num2")

# Using and with if, else statement or conditions

ten = 10
five = 5

if (ten >= five and five ==ten):
    print("True")
else:
    print("False")    # the both conditions has to be true before the system will return true else it will return false


# Using or with if, else statement or conditions

ten = 10
five = 5

if (ten==five or ten>=five):
    ten = 0                     # if True will make ten var = 0
    print("True")
else:
    print("False")


