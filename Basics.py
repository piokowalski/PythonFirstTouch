correct_password = "aezakmi"
personName = input("Enter Your name: ")
password = input("Enter the password: ")

while correct_password != password:
    password = input("Try again, password: ")

message = ("Hello,",personName,"You're logged in.") # Printing as array
print(message)
