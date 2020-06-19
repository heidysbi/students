students = []


# student1 = {
#     'id':1,
#     'name': 'Mario',
#     'age':23,
#     'gender': 'M'
# }
# student2 = {
#     'id':10,
#     'name': 'María',
#     'age':20,
#     'gender': 'F'
# }

# students.append(student1)
# students.append(student2)

#print(students)

while(True):

    print("You want to do?")
    print("a. Enter a new student")
    print("b. Exit")
    print("c. Print the list")


    print("Enter the option")
    option = input()

    if option == "a": 
        print("Enter the student's name")
        name = input()
        print("Enter the student's age")
        age = input()
        print("Enter the student's gender")
        gender = input()

    student = {
        'name': name,
        'age': age,
        'gender': gender
    }
    students.append(student)
    
    
    if option == "b":
        break

    if option == "c":    
        print(students)

    print()
    print("="*100)
    print()

print("The session has ended")
