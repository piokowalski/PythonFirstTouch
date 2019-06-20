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
print(family)
#Adding new single element "Oma" in the end, and "Opa" at 2nd index, and removing "Tante"
