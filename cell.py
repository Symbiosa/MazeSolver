from graphics import Line, Point


class Cell:
    def __init__(self,x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.visited = False

    def draw(self, win):
        wall_color = "black"
        background_color = "white"
        
        left_wall_color = wall_color if self.has_left_wall else background_color
        win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), fill_color = left_wall_color)
        
        top_wall_color = wall_color if self.has_top_wall else background_color
        win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), fill_color = top_wall_color)
        
        right_wall_color = wall_color if self.has_right_wall else background_color
        win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), fill_color = right_wall_color)
        
        bottom_wall_color = wall_color if self.has_bottom_wall else background_color
        win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), fill_color = bottom_wall_color)

    def draw_move(self, to_cell, undo=False):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)