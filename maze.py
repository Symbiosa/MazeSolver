from cell import Cell
from graphics import Window
import time

class Maze:
    def __init__(self, win, num_rows, num_cols):
        self.win = win
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cells = self._create_cells()
        self._break_entrance_and_exit()
        
    def _create_cells(self):
        # Example of creating cells; replace with actual logic.
        cells = []
        for row in range(self.num_rows):
            row_cells = []
            for col in range(self.num_cols):
                # Placeholder for coordinates; replace with actual values.
                x1, y1, x2, y2 = self.calculate_cell_coordinates(row, col) 
                cell = Cell(x1, y1, x2, y2)
                row_cells.append(cell)
            cells.append(row_cells)
        return cells
    
    def calculate_cell_coordinates(self, row, col):
        # Method to calculate x1, y1, x2, y2 for given row and col
        cell_width = 20  # example width, replace as needed
        cell_height = 20  # example height, replace as needed
        x1 = col * cell_width
        y1 = row * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        return x1, y1
    
    def _draw_cell(self, i, j):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        
        self._cells[j][i].draw(x1,y1,x2,y2)
        
        self._animate()
        
    def _animate(self):
        self.win.redraw()
        
        time.sleep(0.1)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw(self.win)
        
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw(self.win)
    