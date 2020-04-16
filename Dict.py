# Make sure to copy and run the codes separately on your editor to see the results

# Using dictionary in python

dic = {"Toyota": "Camry", "Cylinder": "V6"}

print(dic["Toyota"])
print(dic["Cylinder"])

dic2 = {"Cars": ["Toyota", "Mercedes", "Tesla", "Nissan"], "Houses": ["Duplex", "Story Building"]}

print(dic2["Cars"])
print(dic2["Houses"])

dic2["Schools"] = ["UNN", "UNIBEN", "OAU"]
print(dic2["Schools"])


# Adding new value to a dictionary

dic["Colour"] = "White"
print(dic["Colour"])


# filling an empty dictionary

dic3 = {}

dic3["Colour"] = ["Orange", "White", "Indigo", "Violet"]
dic3["Fruits"] = ["Orange", "Pineapple", "Mango", "Bananas"]
dic3["Birds"] = ["Chicken", "Eagle", "Ostrich"]

print(dic3["Colour"])
print(dic3["Fruits"])         # prints the values of the keys in the dictionary
print(dic3["Birds"])

print(dic3)                    # prints the whole dictionary in one line


# editing a value in the dictionary

OS = {"Apple": "Mac", "Microsoft": "Windows", "At%t": "Pc"}

print("Before is" + " " + OS["At%t"])

OS["At%t"] = "Linux"

print(OS)


# Deleting a key from dictionary

print("Before deletion")
print(OS)

print("After Deletion")
del OS["At%t"]
print(OS)

# Using input() function in our program

name = input("What's your name?\n")

print("Hi" + " " + name + " " + "How are you doing?")

user = input()
print("Thank you" + " " + name + " " "have a nice day")
