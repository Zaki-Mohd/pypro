import tkinter as tk

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_point(canvas, point):
    canvas.create_oval(point.x-2, point.y-2, point.x+2, point.y+2, fill="black")

root = tk.Tk()
root.title("Shapes Drawing")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()


point = Point(200, 200)
draw_point(canvas, point)

root.mainloop()
