# Make sure to copy and run the codes separately on your editor to see the results

# Using Function in a python program

def function():
    print("Hello, this code is from the function")

print("this code is from our main program")

function()

# Using parameters and Argument within the function in a program
# Using multiple call in function


def names(Lname, Fname, Mname):               # the names passed here is your parameter
    print("Your Last name is" + " " + Lname)
    print("Your first name is" + " " + Fname)
    print("Your middle name is" + " " + Mname)
    print("\n")                                  #  \n prints the function in a new line

names("Ugwuanyi", "Kenneth", "Oluchi")
names("Ugwuanyi", "Valentine", "Chidubem")
names("Ugwuanyi", "Lynda", "Chisom")              # the names passed here is your argument
names("Ugwuanyi", "Toochukwu", "Celestine")
names("Ugwuanyi", "Jude", "Ebuka")
names("Ugwuanyi", "Earnest","Kelechi")
names("Ugwuanyi", "Jennifer", "Chinemerem")


# Default  values in functions

def you(Lname ="John", Fname ="Oluchi", Mname = "Toochukwu"):               # the names passed here is your parameter
    print("Your Last name is" + " " + Lname)
    print("Your first name is" + " " + Fname)
    print("Your middle name is" + " " + Mname)
    print("\n")

you()

you(Lname="Thomas", Fname="Johnson", Mname="Mia")
you(Mname="Jenson", Lname="Ugwuanyi", Fname="Tricia")


# Return value in function

def addition(a,b):
    total = a + b
    return total    # return here is used to return value through the main program

print(addition(10,5))