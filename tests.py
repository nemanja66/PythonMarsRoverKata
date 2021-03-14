import unittest
import rover
import grid

class RoverShould(unittest.TestCase):

    def test_makeNoMovementWhenPassedEmptyArrayOfCommands(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute(""), "1:1:N")

    def test_rotateRight(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("R"), "1:1:E")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RR"), "1:1:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RRR"), "1:1:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RRRR"), "1:1:N")

    def test_rotateLeft(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("L"), "1:1:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("LL"), "1:1:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("LLL"), "1:1:E")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("LLLL"), "1:1:N")

    def test_moveNorth(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("M"), "1:2:N")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MM"), "1:3:N")

    def test_moveSouth(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MMRRM"), "1:2:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MMMRRM"), "1:3:S")

    def test_moveEast(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RM"), "2:1:E")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMM"), "3:1:E")

    def test_moveWest(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMMRRM"), "2:1:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMMMRRM"), "3:1:W")