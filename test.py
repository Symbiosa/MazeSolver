import unittest
from unittest.mock import MagicMock
from cell import Cell
from graphics import Line, Point

# Mock classes for Point, Line, and the window to draw lines on
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Line:
    def __init__(self, start, end, fill_color):
        self.start = start
        self.end = end
        self.fill_color = fill_color

class MockWindow:
    def draw_line(self, line):
        pass

class TestCellDrawMove(unittest.TestCase):
    def setUp(self):
        # Create a mock window
        self.mock_window = MockWindow()
        self.mock_window.draw_line = MagicMock()
        
        # Create initial cell
        self.cell = MagicMock()
        self.cell.x, self.cell.y = 10, 20
        self.cell.width, self.cell.height = 30, 40
        self.cell._win = self.mock_window
        
    def create_to_cell(self, x, y, width, height):
        # Create destination cell
        to_cell = MagicMock()
        to_cell.x, to_cell.y = x, y
        to_cell.width, to_cell.height = width, height
        return to_cell

    def test_draw_move_red(self):
        to_cell = self.create_to_cell(50, 60, 30, 40)        
        self.cell.draw_move = draw_move.__get__(self.cell)  # Binding function to mock
        self.cell.draw_move(to_cell, undo=False)
        
        # Verify the draw_line was called once
        self.mock_window.draw_line.assert_called_once()
        
        # Capture the line object used in the call
        line = self.mock_window.draw_line.call_args[0][0]
        
        # Verify the coordinates and color
        self.assertEqual(line.start.x, 25)  # (10 + 30/2)
        self.assertEqual(line.start.y, 40)  # (20 + 40/2)
        self.assertEqual(line.end.x, 65)    # (50 + 30/2)
        self.assertEqual(line.end.y, 80)    # (
        self.assertEqual(line.fill_color, "red")

    def test_draw_move_gray(self):
        to_cell = self.create_to_cell(50, 60, 30, 40)
        self.cell.draw_move = draw_move.__get__(self.cell)  # Binding function to mock
        self.cell.draw_move(to_cell, undo=True)
        
        # Verify the draw_line was called once
        self.mock_window.draw_line.assert_called_once()
        
        # Capture the line object used in the call
        line = self.mock_window.draw_line.call_args[0][0]
        
        # Verify the coordinates and color
        self.assertEqual(line.start.x, 25)  # (10 + 30/2)
        self.assertEqual(line.start.y, 40)  # (20 + 40/2)
        self.assertEqual(line.end.x, 65)    # (50 + 30/2)
        self.assertEqual(line.end.y, 80)    # (60 + 40/2)
        self.assertEqual(line.fill_color, "gray")

if __name__ == '__main__':
    unittest.main()
