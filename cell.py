from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
    
    def draw_move(self, to_cell, undo=False):
        # Calculate the center of the current cell and the to_cell
        start = Point((self.x + self.width) / 2, (self.y + self.height) / 2)
        end = Point((to_cell.x + to_cell.width) / 2, (to_cell.y + to_cell.height) / 2)
        
        # Determine the color based on the undo flag
        color = "gray" if undo else "red"
        
        # Create the line object
        line = Line(start, end, fill_color=color)
        
        # Draw the line
        self._win.draw_line(line)
            