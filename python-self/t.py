import tkinter as tk
windows = tk.Tk()
frame = tk.Frame()
frame.master.title("Test")
windows.geometry("300x300")

# label = tk.Button(
#     text="Click me!",
#     fg ="#fff",
#     bg = "#aa44dd",
#     width = 30,
#     height = 5
# )
# entry = tk.Entry(
#     fg  ="#666",
#     bg  ="#aabb12",
#     width = 40
# )

# name = entry.get()
# label.pack()
# entry.pack()
#========================================================================================
#========================================================================================
# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=windows, relief=relief, borderwidth=10)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()

#========================================================================================
#========================================================================================
def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")
button.pack()
button.bind("<Button-1>", handle_click)

windows.mainloop()