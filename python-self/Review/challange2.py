import tkinter as tk
import random

root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)
frame = tk.Frame()
frame.master.title("CHUM")


def draw_a_shap(x, y, size):
    x1 = x - size
    y1 = y - size
    x2 = x + size
    y2 = y + size
    canvas.create_rectangle(x1, y1, x2, y2, fill=random.choice(colors))


colors = ["red", "orange", "yellow", "green",
          "purple", "brown", "blue", "indigo", "violet"]

for top in range(1, 10):
    draw_a_shap(50 * top, 50, 20)
for right in range(1, 10):
    draw_a_shap(500, 50 * right, 20)

for left in range(1, 10):
    draw_a_shap(50, 50 * left, 20)

for buttom in range(1, 11):
    draw_a_shap(50 * buttom, 500, 20)
for row in range(1, 5):
    for col in range(1, 5):
        draw_a_shap(100 * row, 100 * col, 40)

# for row in range(1, 11):
#     for col in range(1, 11):
#         draw_a_shap(50 * row, 50 * col, 20)
canvas.pack(expand=True, fill="both")
root.mainloop()
