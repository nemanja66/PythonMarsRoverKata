import unittest
import rover
import grid
import location

class RoverShould(unittest.TestCase):

    def test_makeNoMovementWhenPassedEmptyArrayOfCommands(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("", 1), "0:0:N")

    def test_rotateRight(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("R", 1), "0:0:E")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RR", 1), "0:0:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RRR", 1), "0:0:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RRRR", 1), "0:0:N")

    def test_rotateLeft(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("L", 1), "0:0:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("LL", 1), "0:0:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("LLL", 1), "0:0:E")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("LLLL", 1), "0:0:N")

    def test_moveNorth(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("M", 1), "0:1:N")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MM", 1), "0:2:N")

    def test_moveSouth(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MMRRM", 1), "0:1:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MMMRRM", 1), "0:2:S")

    def test_moveEast(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RM", 1), "1:0:E")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMM", 1), "2:0:E")

    def test_moveWest(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMMRRM", 1), "1:0:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMMMRRM", 1), "2:0:W")

    def test_wrapAroundNorthEdge(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MMMMMMMMMM", 1), "0:0:N")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MMMMM", 2), "0:0:N")

    def test_wrapAroundEastEdge(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMMMMMMMMMM", 1), "0:0:E")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMMMMM", 2), "0:0:E")

    def test_wrapAroundWestEdge(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("LM", 1), "9:0:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMRRM", 2), "0:0:W")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMRRMMM", 2), "6:0:W")

    def test_wrapAroundSouthEdge(self):
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RRM", 1), "0:9:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MRRMMM", 2), "0:6:S")
        self._grid = grid.Grid(list())
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MRRM", 2), "0:0:S")
    
    def test_stopAndReportObstacleWhenMovesEast(self):
        self._grid = grid.Grid([location.Location(2, 0)])
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMMMMMM", 1), "O:2:0:E")

    def test_stopAndReportObstacleWhenMovesEastAndStepIsGreaterThanCoordinate(self):
        self._grid = grid.Grid([location.Location(2, 0)])
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("RMMMMMM", 4), "O:2:0:E")

    def test_stopAndReportObstacleWhenMovesSouth(self):
        self._grid = grid.Grid([location.Location(0, 8)])
        self._rover = rover.Rover(self._grid)
        self.assertEqual(self._rover.execute("MRRMMMM", 2), "O:0:8:S")