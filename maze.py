from cell import Cell
from point import Point
from window import Window
import time
import random

class Maze:
    def __init__ (self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = [
            [
                Cell(
                    Point(self.x1 + (i * self.cell_size_x), self.y1 + (j * self.cell_size_y)),
                    Point(self.x1 + (i * self.cell_size_x) + self.cell_size_x, self.y1 + (j * self.cell_size_y) + self.cell_size_y),
                    self._win
                )
                for j in range(self.num_cols)
            ]
            for i in range(self.num_rows)
        ]

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]
            possible_directions = []
            
            for direction in to_visit:
                if 0 <= direction[0] < self.num_rows and  0 <= direction[1] < self.num_cols and self._cells[direction[0]][direction[1]].visited == False:
                    possible_directions.append(direction)
            if len(possible_directions) == 0:
                return
            direct = random.choice(possible_directions)

            match (direct[0] - i, direct[1] - j):
                case (0, 1):
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[direct[0]][direct[1]].has_top_wall = False
                case (1, 0):
                    self._cells[i][j].has_right_wall = False
                    self._cells[direct[0]][direct[1]].has_left_wall = False
                case (0, -1):
                    self._cells[i][j].has_top_wall = False
                    self._cells[direct[0]][direct[1]].has_bottom_wall = False
                case (-1, 0):
                    self._cells[i][j].has_left_wall = False
                    self._cells[direct[0]][direct[1]].has_right_wall = False
            self._cells[i][j].draw()
            self._cells[direct[0]][direct[1]].draw()
            self._break_walls_r(direct[0], direct[1])

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        possible_directions = [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]

        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
    
        for direction in possible_directions:
            if 0 <= direction[0] < self.num_rows and  0 <= direction[1] < self.num_cols and self.__has_no_walls_between(i, j, direction[0], direction[1]) and self._cells[direction[0]][direction[1]].visited == False:
                self._cells[i][j].draw_move(self._cells[direction[0]][direction[1]])
                if self._solve_r(direction[0], direction[1]) == True:
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[direction[0]][direction[1]], True)
        return False

    def __has_no_walls_between(self, i1, j1, i2, j2):
        match (i2 - i1, j2 - j1):
            case (0, 1):
                return not(self._cells[i1][j1].has_bottom_wall) and not (self._cells[i2][j2].has_top_wall)
            case (1, 0):
                return not(self._cells[i1][j1].has_right_wall) and not (self._cells[i2][j2].has_left_wall)
            case (0, -1):
                return not(self._cells[i1][j1].has_top_wall) and not (self._cells[i2][j2].has_bottom_wall)
            case (-1, 0):
                return not(self._cells[i1][j1].has_left_wall) and not (self._cells[i2][j2].has_right_wall)