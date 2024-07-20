from cell import Cell
import random
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
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self.solve()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                self._cells[row][col].visited = False
        
    def solve(self):
        start_i, start_j = 0, 0
        end_i, end_j = len(self._cells) - 1, len(self._cells[0]) - 1
        
        self._end_cell_i = end_i
        self._end_cell_j = end_j
        
        return self._solve_r(start_i, start_j)  
    
    def can_move(self, i, j, ni, nj):
        # Determine the direction of the move
        if ni == i - 1 and nj == j:  # Move up
            return not self._cells[i][j].walls['up'] and not self._cells[ni][nj].walls['down']
        elif ni == i + 1 and nj == j:  # Move down
            return not self._cells[i][j].walls['down'] and not self._cells[ni][nj].walls['up']
        elif ni == i and nj == j - 1:  # Move left
            return not self._cells[i][j].walls['left'] and not self._cells[ni][nj].walls['right']
        elif ni == i and nj == j + 1:  # Move right
            return not self._cells[i][j].walls['right'] and not self._cells[ni][nj].walls['left']
        return False
    
    def draw_move(self, i, j, ni, nj):
    # Imagine some logic to draw or log the move from (i, j) to (ni, nj)
        print(f"Moving from ({i}, {j}) to ({ni}, {nj})")

    def draw_undo_move(self, i, j, ni, nj):
    # Imagine some logic to draw or log the undo move
        print(f"Undoing move from ({ni}, {nj}) to ({i}, {j})")
                
    def _solve_r(self,i,j):
        self._cells[i][j].visited = True
        self._animate()
        
        if (i, j) == (self._end_cell_i, self._end_cell_j):
            return True
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for di, dj in directions:
            ni, nj = i + di, j+ dj
        
            if 0 <= ni < len(self._cells) and 0 <= nj < len(self._cells[0]) and not self._cells[ni][nj].visited:
                
                if self.can_move(i, j, ni, nj):
                    
                    self.draw_move(i, j, ni, nj)
                    
                    if self._solve_r(ni, nj):
                        return True
                    
                    self.draw_undo_move(i, j, ni, nj)        
                
        return False