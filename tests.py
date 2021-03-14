import unittest
import rover
import grid

class RoverShould(unittest.TestCase):

    def test_makeNoMovementWhenPassedEmptyArrayOfCommands(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute(""), "0:0:N")

    def test_rotateRight(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("R"), "0:0:E")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RR"), "0:0:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RRR"), "0:0:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RRRR"), "0:0:N")

    def test_rotateLeft(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("L"), "0:0:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("LL"), "0:0:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("LLL"), "0:0:E")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("LLLL"), "0:0:N")

    def test_moveNorth(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("M"), "0:1:N")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MM"), "0:2:N")

    def test_moveSouth(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MMRRM"), "0:1:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MMMRRM"), "0:2:S")

    def test_moveEast(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RM"), "1:0:E")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMM"), "2:0:E")

    def test_moveWest(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMMRRM"), "1:0:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMMMRRM"), "2:0:W")