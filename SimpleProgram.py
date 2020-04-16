# Creating my first simple program

Name = print(input("What is your name? "))
Age = print(input("What is your age? "))
print("Thank you for using my simple program")

# you can use my simple program to calculate the number of days, minutes and second you have being alive on earth

print("Answer this questions to know how long you have lived in this life...")
name = input("Name:")
print("What is your age? ", (name), "?")
age = int(input("age:"))

days = age * 365
minutes = age * 525948
seconds = age * 31556926

print(name, "has being alive for", days, "days", minutes, "minutes", "and", seconds, "seconds")
print("Thank you for using age calculation program")