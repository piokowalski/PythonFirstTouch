correct_password = ""
#personName = input("Enter Your name: ")
personName = "Pyton"
# password = input("Enter the password: ")
password = ""

while correct_password != password:
    password = input("Try again, password: ")

message = ("Hello %s, You're logged in." %personName)
print(message)

print(len(message))
# counting letters

print(message[2])
# printing the 3rd letter in this String

print(message.index("o"))
# showing index of letter "o" is in this String

print (message.replace("Hello", "Hi"))
#replacing "Hello" into "Hi"



print("\n")
# N U M B E R S
# Operations

from math import*

myNum = -7
print(abs(myNum))
#printing absolute valuen

print(pow(myNum, 2))
#power function

print(max(88, -212, myNum))
#printing the biggest valued number

print(round(3.4))
print(round(3.5))
# round operation
print(floor(7.5))
print (ceil(7.5))
#rounding to lower / higher integer - "math import*"