correct_password = "a"
personName = input("Enter Your name: ")
password = input("Enter the password: ")

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

