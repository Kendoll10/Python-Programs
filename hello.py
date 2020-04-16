# lets print a hello world program
# syntax is just like a grammar in the english language and all programming language have that


print("hello world")

for value in range(5):
    print(value)

# using IF and ELSE statement in python

num = -2

if num >= 0:
    print("positive number")
else:
    print("negative number")

# lets look at the string operations in python

String = "Hello python"
String2 = "i love to learn new things"
print(String + ' ' + String2)


# Boolean Values in python

a = True
b = False
print(a)
print(b)

c = not True      # this means false
d = not False     # this means true
print(c)
print(d)

# lets discuss about using the 'IN' and 'NOT IN' operator in python

animal = "goat"
if animal not in ["lion", "cat"]:
    print("your animal is not in the list")

bird = "Ostrich"
if bird in ["chicken", "Turkey", "Ostrich"]:
    print("your bird is in the list")

List = ["Books", "Apple", "Dog", "Camel"]
List.reverse()
print(List)



