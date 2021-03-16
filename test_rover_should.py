import pytest
from rover import Rover
from grid import Grid
from location import Location

def test_makeNoMovementWhenPassedEmptyArrayOfCommands():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("", 1) == "0:0:N"

def test_rotateRight():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("R", 1) == "0:0:E"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RR", 1) == "0:0:S"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RRR", 1) == "0:0:W"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RRRR", 1) == "0:0:N"

def test_rotateLeft():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("L", 1) == "0:0:W"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("LL", 1) == "0:0:S"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("LLL", 1) == "0:0:E"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("LLLL", 1) == "0:0:N"

def test_moveNorth():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("M", 1) == "0:1:N"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("MM", 1) == "0:2:N"

def test_moveSouth():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("MMRRM", 1) == "0:1:S"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("MMMRRM", 1) == "0:2:S"

def test_moveEast():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RM", 1) == "1:0:E"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RMM", 1) == "2:0:E"

def test_moveWest():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RMMRRM", 1) == "1:0:W"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RMMMRRM", 1) == "2:0:W"

def test_wrapAroundNorthEdge():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("MMMMMMMMMM", 1) == "0:0:N"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("MMMMM", 2) == "0:0:N"

def test_wrapAroundEastEdge():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RMMMMMMMMMM", 1) == "0:0:E"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RMMMMM", 2) == "0:0:E"

def test_wrapAroundWestEdge():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("LM", 1), "9:0:W"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RMRRM", 2), "0:0:W"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RMRRMMM", 2), "6:0:W"

def test_wrapAroundSouthEdge():
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("RRM", 1) == "0:9:S"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("MRRMMM", 2) == "0:6:S"
    grid = Grid(list())
    rover = Rover(grid)
    assert rover.execute("MRRM", 2) == "0:0:S"

def test_stopAndReportObstacleWhenMovesEast():
    grid = Grid([Location(2, 0)])
    rover = Rover(grid)
    assert rover.execute("RMMMMMM", 1) == "O:2:0:E"

def test_stopAndReportObstacleWhenMovesEastAndStepIsGreaterThanCoordinate():
    grid = Grid([Location(2, 0)])
    rover = Rover(grid)
    assert rover.execute("RMMMMMM", 4) == "O:2:0:E"

def test_stopAndReportObstacleWhenMovesSouth():
    grid = Grid([Location(0, 8)])
    rover = Rover(grid)
    assert rover.execute("MRRMMMM", 2) == "O:0:8:S"