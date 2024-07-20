from cell import Cell
from graphics import Window
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self.win = win
        self._create_cells()
        self._break_entrance_and_exit()
        
    def _create_cells(self):
        self._cells = [] #New list to hold the matrix
        for col in range(self.num_cols): #Iterating through num of cols
            column = [] #Creating new column list for each iteration
            for row in range(self.num_rows): #Iterating through num of rows
                cell = Cell(self.win)
                x = self.x1 + col * self.cell_size_x #Calculate x 
                y = self.y1 + row * self.cell_size_y #Calculate y
                
                #cell = Cell(x,y,self.num_cols, self.num_rows) #Creating new Cell with given arguements
                
                #self._draw_cell(row,col) #Draw cell using _draw_cell() method
                
                column.append(cell) #Appending given Cell to column list
            self._cells.append(column) #Appending populated column list to matrix
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(row,col)
 
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
    