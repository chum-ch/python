
# lastValue = array[0]
# result = ""
# foundError = False
# for index in range(1, len(array)):
#     if array[index] < array[index-1]:
#         foundError = True
# if not foundError:
#     print("Ascending")
# else:
#     print("Error")
#==================================================================
#==================================================================

# text = "chum [10] live [in] pv"
# mytext = ""
# befor = False
# start = 0
# end = 0
# for index in range(len(text)):
#     if text[index] == "[":
#         start = index
#         if not befor:
#             mytext += text[0:start]
#             befor = True
#         else:
#             mytext += text[end+1: start]
#     elif text[index] == "]":
#         end = index  
# print(mytext + text[end+1:])

#==================================================================
#==================================================================
# text = "chum [dd] p [2] w"
# result = ""
# commentMode = False
# for char in text:
#     if char == "[":
#         commentMode = True
#     elif char == "]":
#         commentMode = False
#     else:
#         if not commentMode:
#             result += char
# print(result)
#==================================================================
#==================================================================

# array = [0, 0, 0, 0, 0, 1]
# direction = "L"   # can be "R" or "L"
# if array[0] == 1 and direction == "L":
#     print(array)
# elif array[-1] == 1 and direction == "R":
#     print(array)
# else:
#     # 1 - Find the index of 1
#     indexOfOne = -1
#     for index in range(len(array)) :
#         if array[index] == 1:
#             indexOfOne = index

#     # 2 - Update the array

#     if direction == "R" :
#         array[indexOfOne+1] = 1
#         array[indexOfOne] = 0
#     elif direction == "L" :
#         array[indexOfOne-1] = 1
#         array[indexOfOne] = 0
#     # 3 - Print array
#     print(array)
#==================================================================
#==================================================================

## switch value

# array = [2,4,6]
# array[1], array[2], = array[2], array[1]
# print(array)

#==================================================================
#==================================================================

# array = [0,0,1,0,0,0,0]
# action = input("Enter action: ")
# if array[0] == 1 and action.upper() == "L":
#     print(array)
# elif array[-1] == 1 and action.upper() == "R":
#     print(array)
# else:
#     conunt_action = 0
#     index_of_one = 0
#     for index in range(len(array)):
#         if array[index] == 1:
#             index_of_one = index
#     for char in action:
#         if char.upper() == "R":
        
#                 conunt_action += 1
#         else:
         
#                 conunt_action -= 1
#     if conunt_action == 0:
#         print(array)
#     elif conunt_action < 0 or conunt_action > len(array):
#         print("Action out of range!")
#     else:
#         array[index_of_one] = 0
#         array[index_of_one + conunt_action] = 1
#         print(array)

#==================================================================
#==================================================================
import tkinter as tk
import random

# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("550x200")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Hello PNC")
canvas = tk.Canvas(frame)

def myEventTrigger(event):
    print("User clicked at positon: ", event.x, event.y)
    randomColor = random.choice(colors)
    canvas.itemconfig(oval, fill=random.choice(colors))
    canvas.move(oval, 10, 10)

colors = ["red", "orange", "yellow", "green", "purple", "brown", "blue", "indigo", "violet","FireBrick","DeepPink","Chartreuse"]

oval = canvas.create_oval(50, 50, 300, 300, fill="red", tags)
# pack means "draw what i put inside"



canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()