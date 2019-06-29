# Catching the exceptions
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Input is invalid!")


try:
    value = 10/0
    digit = int(input("Digit please: "))
    print(digit)
except ZeroDivisionError:
    print("Divided by zero, cholero")
except ValueError:
    print("Invalid digit!")