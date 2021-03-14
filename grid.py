import location
from option import Result, Ok, Err

class Grid():
    def __init__(self, obstacles):
        self.northEdge = 10
        self.westEdge = 10
        self._obstacles = obstacles

    def nextLocationFor(self, inputLocation, direction, step):
        if direction.symbol() == "N":
            for s in range (step):
                inputLocation.y = inputLocation.y + 1
                _location = location.Location(inputLocation.x, inputLocation.y % self.northEdge)
                if self.isObstacle(_location): return Result.Err(_location)
            return Result.Ok(_location)
        elif direction.symbol() == "S":
            for s in range (step):
                inputLocation.y = inputLocation.y - 1 if inputLocation.y > 0 else self.northEdge - 1
                _location = location.Location(inputLocation.x, inputLocation.y)      
                if self.isObstacle(_location): return Result.Err(_location)  
            return Result.Ok(_location)
        elif direction.symbol() == "E":
            for s in range (step):
                inputLocation.x = inputLocation.x + 1
                _location = location.Location(inputLocation.x % self.westEdge, inputLocation.y)
                if self.isObstacle(_location): return Result.Err(_location)
            return Result.Ok(_location)
        elif direction.symbol() == "W":
            for s in range (step):
                inputLocation.x = inputLocation.x - 1 if inputLocation.x > 0 else self.westEdge - 1
                _location = location.Location(inputLocation.x, inputLocation.y)
                if self.isObstacle(_location): return Result.Err(_location)
            return Result.Ok(_location)

    def isObstacle(self, location):
        return location in self._obstacles

        