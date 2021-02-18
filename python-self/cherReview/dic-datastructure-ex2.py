students = [
    {
        "name": "Bunthoeun", 
        "score": 98
    },
    {
        "name": "Sophea", 
        "score": 95
    },
    {
        "name": "Dyna", 
        "score": -12
    },
    {
        "name": "Chanthy", 
        "score": 25
    },
]

# bestStudents array should contains the name of students with score greater than 75
# goodStudents array should contains the name of students with score lower than 75
# Put your code below

# Display the lists
bestStudents = []
goodStudents = []
for index in range(len(students)):
    if students[index]["score"] > 75:
        bestStudents.append(students[index]["name"])
    else:
        goodStudents.append(students[index]["name"])
print("Best students : ", bestStudents)
print("Good students : ", goodStudents)