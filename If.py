# a = input("Enter first number: ")
# b = input("Enter second number: ")

a = 4 #float(a)
b = 6 #float(b)
c = "" #""
x = "*" #input("Enter an operator: ")

if x == "+" :
    c = a + b
    print(c)
elif x == "-" :
    c = a - b
    print(c)
elif x == "*" :
    c = a * b
    print("Result is: ")
    print(c)
elif x == "/" :
    c = a / b
    print(c)
elif x == "%" :
    c = a % b
    print(c)
else:
    c = "Try again with operator"
    print("Answer: ", c)

# B A S I C S below:
is_boy = True
is_tall = False
is_ok = False

if is_boy and is_tall:
    print("Eligible.")
else:
    print("Denied.")

if is_boy or is_tall:
    print("Eligible.")
else:
    print("Denied.")