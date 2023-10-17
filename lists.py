Students = ["Cynthia", "Olive", "Khadija", "Lisa"]
print(len(Students))
Students_two = ["Ruth", "Becky"]

# prints the last item
print(Students[-1])

# find the first item
print(Students[0])

# 3rd element
print(Students[3])

# insert students names
Students.insert(0, "Anne")
print(Students)

# extends
Students.extend(Students_two)
print(Students)
print(Students[-1])

# remove students
Students.remove(Students[-1])
print(Students)
print(Students[:2])

if "Abbie" in Students:
    print("He is an existing students")
else:
    print("Student does not exist")

# deletes students at index 0
del Students[0]
print(Students)


# working with empty list
empty_list =[]

# defining maximum number of data to expect
max_user = int(input("Enter maximum number of data required: "))

for i in range(0, max_user):
    new_user = int(input())
    empty_list.append(new_user)

    print(empty_list)