correct_password = "aezakmi"
personName = input("Enter Your name: ")
password = input("Enter the password: ")

while correct_password != password:
    password = input("Try again, password: ")

message = ("Hello %s, You're logged in." %personName)
print(message)

print(len(message))
# counting letters