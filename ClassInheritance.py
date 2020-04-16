# Make sure to copy and run the codes separately on your editor to see the results
# Class inheritance

class Person():
    def __init__(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("your name is" + " " + self.name + " " + "your age is" + " " + self.age + " " + "your I.D number is" + " " + self.idNum)

class Man():
    def strong(self):
        print("Men are strong")


class Child(Person, Man):
    pass
kid = Child("Frank", "4", "295749304")
kid.output()

kid.strong() 





