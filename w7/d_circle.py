import tkinter as tk

class Circle:
    def __init__(self, x, y, radius, color="black"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

def draw_circle(canvas, circle):
    canvas.create_oval(circle.x-circle.radius, circle.y-circle.radius, circle.x+circle.radius, circle.y+circle.radius, fill=circle.color)


root = tk.Tk()
root.title("Shapes Drawing")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()


circle = Circle(300, 300, 50, color="red")
draw_circle(canvas, circle)

root.mainloop()
