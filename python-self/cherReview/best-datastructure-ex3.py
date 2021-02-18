print("Welcome to the student database")
print("0: exit")
print("1: add student to database with score 0")
print("2: add points to one student")
print("3: print student average")
print("4: print all students and score")
action = int(input("select an action : "))
students = []
# I want to update the condd
conindexOfTheStudents = -1
outPutNameWithIndex = ""
while action != 0:
    if action == 1:
        # TODO :   - ask for the name of student, 
        #          - create a student with this name and with score=0 
        #          - append the new student to the students array
        name = input("Enter the name you want to add more: ")
        dic = {}
        dic["name"] = name
        dic["score"] = 0
        students.append(dic)
        conindexOfTheStudents += 1
        outPutNameWithIndex += "Name of the student is: " + students[conindexOfTheStudents]["name"] + " and the index is: " + str(conindexOfTheStudents) + "\n"
    elif action == 2:
        # TODO :   - ask for the index of student, 
        #          - ask how many score to add
        #          - add score to the student in array
        print(outPutNameWithIndex)
        studentsIndex = int(input("Enter index you want ot edit: "))
        addScore = int(input("Enter the scores you want add: "))
        for index in range(len(students)):
            if index == studentsIndex:
                students[index]["score"] += addScore

    elif action == 3:
        # TODO :   - calculate and print average score
        average = 0
        average += students[conindexOfTheStudents]["score"]
        print("The averages of the students is: ", average / len(students))
    elif action == 4:
        print(students)
        print(outPutNameWithIndex)
    action = int(input("select an action : "))
