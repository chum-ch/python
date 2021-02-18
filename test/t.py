# import tkinter as tk
# import random

# root = tk.Tk() 
# root.geometry("600x600")
# canvas = tk.Canvas(root)

# def draw_oval(x, y, size) :
#     x1 = x - size
#     y1 = y - size
#     x2 = x + size
#     y2 = y + size
#     oval = canvas.create_oval(x1, y1, x2, y2, fill="red", tags="move_positon")
# def onButton():
#     # button.showinfo("Hello", "Red Button clicked")
#     draw_oval(300, 300, 30)
#     canvas.itemconfig(oval, fill="red")
#     canvas.move(oval, 0, -20)
#     canvas.tag_bind(" move_positon", "<Button-1>", move_positon)
# button = tk.Button(
#     root,
#     text ="CLEAR ALL",
#     command = onButton,
#     fg = "#ad8922",
#     bg ="#999"
# )


# button.pack()
# canvas.pack(expand=True, fill='both')
# root.mainloop()

import random
colors = ['blue', 'red', 'green', 'banana']

# WAY 1
secret_color = random.randrange(0, len(colors))
print("Colors is:", colors[secret_color])
# WAY 2
print("Color is: ", random.choice(colors))
# WAY 3
shuffle_color = random.shuffle(colors)
print(colors[0])