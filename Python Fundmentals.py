#====================================================================================================
print("")
print("----------Commands----------")
print("")
#====================================================================================================
#Commands ~ This is the Verb of the language, action the computer takes.
#Parameters ~ This is the Adverb of the language, adding more detail to how the computer completes the task.

print("Hello World")

#====================================================================================================
print("")
print("----------Variables----------")
print("")
#====================================================================================================
#Variables make it a lot easier for us to store, recall and modify data. It also allows us to keep thing consistent across our code in case we wish to modify it.

firstName = "John"
lastName = "Doe"
age = "10"
favCol = "Blue"
favFood = "Pizza"
disFood = "Carrots"

print("My name is " + firstName + " " + lastName + ", and I am " + age + " years old!" )
print(f"I really like the colour {favCol}, it's a very nice colour.")
print(f"I love {favFood}, it is the best food in the whole world. I much rather {favFood} then {disFood}")

#====================================================================================================
print("")
print("----------Data Values----------")
print("")
#====================================================================================================

#String ~ Words and letters
print("This is a String")

#Integers ~ Any whole number
print(20)

#Floats ~ Any fractional Number
print(3.149265)

#Boolean ~ True or False
print(True)

#Null ~ No value
print(None)

#We can also use Commands to change the data type.
print(str(2) + str(2))
print(int(3.1425))
print(float(6))

#====================================================================================================
print("")
print("----------Math----------")
print("")
#====================================================================================================
#Computers are really great at math, we can use computers to preform many types of math equations

x = 5
y = 2

#Addition
print(x + y)

#Subtraction
print(x - y)

#Multiplication
print(x * y)

#Division
print(x / y)

#Modulus
print(x % y)

#Exponentiation
print(x ** y)

#Floor Division
print(x // y)

#====================================================================================================
print("")
print("----------Operators----------")
print("")
#====================================================================================================
#Operators are used to assign 

x = 10
print(x)

x += 10
print(x)

x -= 15
print(x)

x *= 5
print(x)

x /= 5
print(x)

x %= 3
print(x)

x //= 10
print(x)

#====================================================================================================
print("")
print("----------Lists----------")
print("")
#====================================================================================================
#List is a very special Data type. Unlike the other data type, Lists can hold mutiple values at once

list = ["Apple", "Bread", "Cheese", "Lettus"]
print(list)

print(list[3])

list.append("Beef")
print(list)

list.remove("Apple")
print(list)

list.pop(1)
print(list)

#====================================================================================================
print("")
print("----------Dictionary----------")
print("")
#====================================================================================================
#like a list but each value has two parts. Think of these parts as the word and the definition

personBio = {
    "First Name" : "John",
    "Last Name" : "Doe",
    "Age" : 20,
    "Favourite Colour" : "Blue",
    "Favourite Food" : "Pizza",
    "Least Favourite Food" : "Carrots"
}
print(personBio)

print(f"My name is {personBio["First Name"]} {personBio['Last Name']}, and I am {str(personBio['Age'])} years old!" )
print(f"I really like the colour {personBio['Favourite Colour']}, it's a very nice colour.")
print(f"I love {personBio["Favourite Food"]}, it is the best food in the whole world. I much rather {personBio["Favourite Food"]} then {personBio["Least Favourite Food"]}")

#====================================================================================================
print("")
print("----------Loops----------")
print("")
#====================================================================================================
#
x = 10

#For Loops
for i in range(x):
    print(f"This message has repeated {i} times.")

#While Loops
while x > 0:
    x -= 1
    print(f"This message will repeat {x} more times")

#====================================================================================================
print("")
print("----------Logic----------")
print("")
#====================================================================================================
#

#If
x = 10
if x == 0:
    print("I will not get printed")

#Else
if x == 0:
    print("I will print if the value of x is 0")
else:
    print("I will print if the value of x is anything but 0")

#Else If
if x == 0:
    print("I will print if the value of x is 0")
elif x == 10:
    print("I will print if the value of x is 10")
else:
    print("I will print if the value of x is anything but 0 or 10")

#Switch

#Try and Except

#====================================================================================================
print("")
print("----------Functions----------")
print("")
#====================================================================================================

