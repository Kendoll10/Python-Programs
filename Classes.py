# Make sure to copy and run the codes separately on your editor to see the results
# Using classes in python
# class instances

class Person ():
    # its always better to make the class name capital just like in person
    def insert(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum     # Indentation is very important don't forget that

    def output(self):
        print("Your name is" + " " + self.name + " " + "your age is" + " " + self.age + " " + "your I.D number is" + " " + self.idNum)

j = Person()
j.insert("John", "44", "1209876")
j.output()

# to access class objects, variables or functions
print(j.name)

# creating multiple instances of a class

p = Person()
p.insert("Greg", "46", "845637")
p.output()

z = Person()
z.insert("Frank", "90", "09152637")
z.output()



#  __init__(self) function or the constructor of the class

class Human():
    def __init__(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum
    def outcome(self):
        print("Your name is " + self.name + " your age is " + self.age + " your I.D number is " + self.idNum)

john = Human("Thomas", "45", "56982389")
# note that we passed the argument to the constructor of the class

john.outcome()


# to access class objects, variables or functions

print(john.name)
print(john.age)
print(john.idNum)
# we use the "dot" to access variable or function


# creating multiple instances of a class

k = Human("James", "56", "122345567")
m = Human("Mia", "26", "983567")

k.outcome()
m.outcome()