from window import Window
from cell import Cell
from point import Point
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, num_rows=10, num_cols=10, cell_size_x=50, cell_size_y=50, win=win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()
main()