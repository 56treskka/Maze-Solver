from point import *
from window import Window

class Cell:
    def __init__(self, point1, point2, window=None, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y
        self._win = window
        self.visited = False
    
    def draw(self):
        if self._win is None:
            return
        
        if self.has_left_wall:
            self._win.draw_line(Line(point1=Point(self._x1, self._y1), point2=Point(self._x1, self._y2)), "black")
        else:
            self._win.draw_line(Line(point1=Point(self._x1, self._y1), point2=Point(self._x1, self._y2)), "white")

        if self.has_right_wall:
            self._win.draw_line(Line(point1=Point(self._x2, self._y1), point2=Point(self._x2, self._y2)), "black")
        else:
            self._win.draw_line(Line(point1=Point(self._x2, self._y1), point2=Point(self._x2, self._y2)), "white")

        if self.has_top_wall:
            self._win.draw_line(Line(point1=Point(self._x1, self._y1), point2=Point(self._x2, self._y1)), "black")
        else:
            self._win.draw_line(Line(point1=Point(self._x1, self._y1), point2=Point(self._x2, self._y1)), "white")

        if self.has_bottom_wall:
            self._win.draw_line(Line(point1=Point(self._x1, self._y2), point2=Point(self._x2, self._y2)), "black")
        else:
            self._win.draw_line(Line(point1=Point(self._x1, self._y2), point2=Point(self._x2, self._y2)), "white")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        if undo == False:
            self._win.draw_line(Line(point1=Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2), point2=Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)), "red")
        else:
            self._win.draw_line(Line(point1=Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2), point2=Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)), "gray")