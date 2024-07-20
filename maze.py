from cell import Cell
import random

class Maze:
    def __init__(self, win, num_rows, num_cols, seed = None, padding = 10):
        self.win = win
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.padding = padding
        self.seed = seed
        if self.seed != None:
            self.seed = random.seed(seed)
        self._cells = self._create_cells()
        self._draw_all_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(self.num_rows, self.num_cols)

    def _draw_all_cells(self):
        for row in self._cells:
            for cell in row:
                cell.draw(self.win)
    
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
        x1 = col * cell_width + self.padding
        y1 = row * cell_height + self.padding
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        return x1, y1, x2, y2
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw(self.win)
        
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw(self.win)
    
    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        
        while True:
            possible_directions = []
            
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append((i-1,j))
            if i < self.num_rows - 1 and not self._cells[i+1][j].visited:
                possible_directions.append((i+1,j))
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i,j-1))
            if j < self.num_cols -1 and not self._cells[i][j+1].visited:
                possible_directions.append((i,j+1))
            
            if not possible_directions:
                return
            
            
            next_i, next_j = random.choice(possible_directions)
            
            self._break_walls_r(next_i, next_j)