from Student import Student

student1 = Student("Michael", "Computer science", 3.2)
student2 = Student("Pamela", "Art", 3.9)

print(student1.on_honor_roll())
print(student2.on_honor_roll())

student1.make_excuse()