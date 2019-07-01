#opening files in Python

counting_file = open("Open_File.txt", "r")
# r - read, w - write, r+ - read/write, a - adding new lines in the file
# print(counting_file.read())

# print(counting_file.readline())
# print(counting_file.readline())

# print(counting_file.readline()[0])
# print(counting_file.readlines()[0])

for line in counting_file.readlines():
    print(line)

counting_file.close()

#Writing to the file - "a" appending
write_file = open("Opening_files_writing","a")

write_file.write("This is a new line created by python, tsssss.")
write_file.write("\nThis is another line created by python, tsssss.")
#the new line needs to be created

write_file.close()