array = [0,1,0,0,0]
action = input("Enter action: ")

if array[0] == 1 and action.upper() =="L":
    print(array)
elif array[-1] == 1 and action.upper() == "R":
    print(array)
else:
    count_r = 0
    count_l = 0
    for index in range(len(array)):
        if array[index] == 1:
            array[index] = 0
            for index1 in range(len(action)):
                if action[index1].upper() == "R":
                    count_r += 1
                elif action[index1].upper() == "L":
                    count_l += 1

