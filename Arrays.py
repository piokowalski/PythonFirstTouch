family = ["Mutter", "Vater", "Tante", "Schwester"]
print(family)
# printing all array

print(family[2:])
# printing members from index 2 and higher

print(family[0:2])
# printing members from index 0 to 1 ( x<2 )

print("\n")

numbers = [12, 52, -4, 9.4, 999]
family.extend(numbers)
print(family)
#Extending one array with another

family.append("Oma")
family.insert(1, "Opa")
family.remove("Tante")

# family.clear()
# #clearing all array

print(family)
#Adding new single element "Oma" in the end, and "Opa" at 2nd index, and removing "Tante"
print(family.index(999))
#Index of element with value 999

print("\n")
#Sorting of values inside

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)


print("\n")
#copying
numbersCopy = numbers.copy()
print(numbersCopy)
print()

#Two dimensional list, with access to it

numbers_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(numbers_grid[0][1])