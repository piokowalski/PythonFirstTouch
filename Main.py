a = input("Enter first number: ")
b = input("Enter second number: ")

a = float(a)
b = float(b)
c = ""
x = input("Enter an operator: ")
if x == "+" :
    c = a + b

elif x == "-" :
    c = a - b

elif x == "*" :
    c = a * b

elif x == "/" :
    c = a / b

elif x == "%" :
    c = a % b
else:
    c = "Try again with operator"
    print("Answer: ", c)