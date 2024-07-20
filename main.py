from graphics import Window
from cell import Cell
from maze import Maze


# def main():
#     win = Window(800, 600)

#     c1 = Cell(win)
#     c1.has_right_wall = False
#     c1.draw(50, 50, 100, 100)

#     c2 = Cell(win)
#     c2.has_left_wall = False
#     c2.has_bottom_wall = False
#     c2.draw(100, 50, 150, 100)

#     c1.draw_move(c2)

#     c3 = Cell(win)
#     c3.has_top_wall = False
#     c3.has_right_wall = False
#     c3.draw(100, 100, 150, 150)

#     c2.draw_move(c3)

#     c4 = Cell(win)
#     c4.has_left_wall = FalseS
#     c4.draw(150, 100, 200, 150)

#     c3.draw_move(c4, True)

#     win.wait_for_close()

def main():
    win = Window(800,600)
    x1, y1 = 50,50
    num_rows, num_cols = 13,7
    cell_size_x, cell_size_y = 40,40
    
    maze = Maze(x1,y1, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._create_cells()
    
    win.wait_for_close()

main()
