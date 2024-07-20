import unittest
import random
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_visited(self):
        num_cols = 10
        num_rows = 10
    # Initialize the Maze
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._reset_cells_visited()
    
    # Confirm every cell in the maze has been reset
        for row in range(num_rows):
            for col in range(num_cols):
                self.assertEqual(
                    m1._cells[row][col].visited,
                    False,
                    f"Cell at ({row}, {col}) was not reset"
            )

# And optionally add the specific cell check with a random number
        random_number = random.randint(0, num_rows - 1)
        self.assertEqual(
            m1._cells[random_number][random_number].visited,
            False,
)

if __name__ == "__main__":
    unittest.main()
