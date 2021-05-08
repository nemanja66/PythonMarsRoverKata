import pytest
from rover import Rover
from grid import Grid
from location import Location
from navigation import Navigation

def test_makeNoMovementWhenPassedEmptyArrayOfCommands():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("") == "0:0:N"

def test_rotateRight():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("R") == "0:0:E"
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RR") == "0:0:S"
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RRR") == "0:0:W"
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RRRR") == "0:0:N"

def test_rotateLeft():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("L") == "0:0:W"
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("LL") == "0:0:S"
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("LLL") == "0:0:E"
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("LLLL") == "0:0:N"

def test_moveNorth():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("M") == "0:1:N"
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("MM") == "0:2:N"

def test_moveSouth():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("MMRRM") == "0:1:S"
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("MMMRRM") == "0:2:S"

def test_moveEast():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RM") == "1:0:E"
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RMM") == "2:0:E"

def test_moveWest():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RMMRRM") == "1:0:W"
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RMMMRRM") == "2:0:W"

def test_wrapAroundNorthEdge():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("MMMMMMMMMM") == "0:0:N"

def test_wrapAroundEastEdge():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RMMMMMMMMMM") == "0:0:E"

def test_wrapAroundWestEdge():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("LM"), "9:0:W"

def test_wrapAroundSouthEdge():
    grid = Grid(list())
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RRM") == "0:9:S"

def test_stopAndReportObstacleWhenMovesEast():
    grid = Grid([Location(2, 0)])
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RMMMMMM") == "O:2:0:E"

def test_stopAndReportObstacleWhenMovesSouth():
    grid = Grid([Location(0, 8)])
    navigation = Navigation(grid)
    rover = Rover(navigation)
    assert rover.execute("RRMMMM") == "O:0:8:S"