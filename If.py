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

def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))