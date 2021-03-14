import location

class Grid():
    def __init__(self, obstacles):
        self.northEdge = 10
        self.westEdge = 10
        self._obstacles = obstacles

    def nextLocationFor(self, inputLocation, direction, step):
        if direction.symbol() == "N":
            return location.Location(inputLocation.x, (inputLocation.y + step) % self.northEdge)
        elif direction.symbol() == "S":
            y = inputLocation.y - step if inputLocation.y >= step else self.northEdge - (step - inputLocation.y)
            return location.Location(inputLocation.x, y)
        elif direction.symbol() == "E":
            return location.Location((inputLocation.x + step) % self.westEdge, inputLocation.y)
        elif direction.symbol() == "W":
            x = inputLocation.x - step if inputLocation.x >= step else self.westEdge - (step - inputLocation.x)
            return location.Location(x, inputLocation.y)