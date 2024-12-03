from tkinter import Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.first = point1
        self.second = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.first.x, self.first.y, self.second.x, self.second.y,
            fill=fill_color, width=2
        )