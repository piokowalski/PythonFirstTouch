
# keyword in Python = def

user = "Jonasz"

def say_hi():
     print("Hello %s !" %user)

say_hi()
print("\n")



#adding values into functions (like in JAVA)

def user_logged(name):
     print(name +" logged in.")


user_logged("Administrator")
user_logged("User")


# return in functions

def cube(numba):
     return numba*numba*numba
     print("It's not going to be printed - must be before return!")


print(cube(4))
#Returning cube of number

result = cube(5)
print(result)
#other method to call this function