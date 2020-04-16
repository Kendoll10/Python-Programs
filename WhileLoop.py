# Make sure to copy and run the codes separately on your editor to see the results

# Using while loop in our python program

i=1
while i<=6:
    print(i)
    i+=1


# using flag to stop looping in python

i = ""
name = "What is your name?\n"

 while (i != "q"):
    i = input(name)      # this programme will keep on looping unless you enter the value "q"


# Using infinite loop in a programme

i = 1

while (i==1):
    name = input("Enter your name: ")
    print("Your name is" + " " + name)    # usually not a good practice in programming


# Using break and continue with while loop

I = 1
user = ""

while (i<=5):
    user = input("Insert any name: ")
    print("You inserted" + " " + user)
    if (user == "John"):
        break
    elif (user == "Mic"):
        continue
    I+=1




