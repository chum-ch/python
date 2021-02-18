

array = [0,1,0,0,0,0,0]
action = input("Enter the action: ")
if array[0] == 1 and action.upper() == "L":
    print("We cannot move!")
elif array[-1] == 1 and action.upper() == "R":
    print("We cannot move!")
else:
    untill = True
    while untill:
        index_of_one = 0
        for index_array in range(len(array)):
            if array[index_array]:
                index_of_one = index_array
                array[index_array] = 0
        for character in action:
            if character.upper() == "R":
                if index_of_one < len(array) -1:
                    index_of_one += 1
            elif character.upper() == "L":
                if index_of_one > 0:
                    index_of_one -= 1
        array[index_of_one] = 1
        print(array)
        action = input("Enter the action: ")