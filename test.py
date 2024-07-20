import unittest
from maze import Maze
from graphics import Window
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800,600)
        x1, y1 = 50,50
        num_rows, num_cols = 10,10
        cell_size_x, cell_size_y = 40,40
        m1 = Maze(x1,y1, num_rows, num_cols, cell_size_x, cell_size_y, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
if __name__ == "__main__":
    unittest.main()
    
# win = Window(800,600)
# x1, y1 = 50,50
# num_rows, num_cols = 13,7
# cell_size_x, cell_size_y = 40,40

# maze = Maze(x1,y1, num_rows, num_cols, cell_size_x, cell_size_y, win)
# maze._create_cells()

# win.wait_for_close()