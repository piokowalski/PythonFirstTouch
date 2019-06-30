#opening files in Python

counting_file = open("Open_File.txt", "r")
# r - read, w - write, r+ - read/write, a - adding new lines in the file
# print(counting_file.read())

print(counting_file.readline())
print(counting_file.readline())

print(counting_file.readlines())
counting_file.close()