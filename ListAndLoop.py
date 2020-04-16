# Make sure to copy and run the codes separately on your editor to see the results

# list and for loop in python

animals = ["lion", "tiger", "dog", "parrot"]
print(animals)

# iif you want to print a specific animal from the list you can use the below method
print(animals[3].title())

# Another way to print an element from the would be
print(animals[-3].title())

# Combining and element of a list with the string
message = "I love my"
print(message + ' ' + animals[2].title())

# you can also print it this way
print("I love my" + " " + animals[-2].title())


# Changing and element from a list
animals[3] = "cat"
animals[0] = "monkey"
print(animals)

# Deleting an element from a list
Toyota = ["camry", "corolla", "nissan"]
del Toyota[-1]
del Toyota[0]
print(Toyota)


# Using sort() and reverse() method in python
List = ["Book", "Apple", "Dog", "Camel"]
List.sort()
print(List)                                  # sorts the list alphabetically

List.sort(reverse=True)
print(List)                                  # this sorts the list alphabetically but in a reverse direction

List.reverse()
print(List)                                 # this reverses the list without sorting it

List.sort(reverse=False)
print(List)                                # this sorts the list alphabetically


# Using the len() method in python
print(len(List))                         # prints out the length of the list or the number of words in the list


# Using for loop with list in python
Fruits = ["Book", "Apple", "Dog", "Camel"]
for value in Fruits:
    print("I love my" + ' ' + value)
print("thank you for using my loop in python")      # this function loops through the list


# Using for loop with range method in python
for values in range(1,5):
    print(values)                               # prints the range of the value from 1-4


# Using min, max, sum with numbers in the list
ListNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(ListNum))                            # prints the minimum number in the list
print(max(ListNum))                            # prints the maximum number in the list
print(sum(ListNum))                            # adds the numbers in the list


# Making a slicing[:] list
OS = ["Mac", "Window", "Linux", "Android", "iOS"]
print(OS[0:5])
print(OS[:3])
print(OS[2:3])      # you can take out the code, paste them on your editor and run the code to see the result
print(OS[2:])
print(OS[:-3])


# Using for loop with slicing list
OS = ["Mac", "Window", "Linux", "Android", "iOS"]
for value in OS[0:5]:
    print(value)


# copying lists using slicing lists
ProgLang = ["C++", "Python", "Php", "Swift4"]
Cpy_ProgLang = ProgLang[:]

print("Printing programming language here")
print(ProgLang)

print("printing the copy slicing list here")
#print(Cpy_ProgLang)

Cpy_ProgLang.append("Java")
print(Cpy_ProgLang)

