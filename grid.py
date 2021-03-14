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
            return location.Location(inputLocation.x, if inputLocation.y > step: inputLocation.y - step else: self.northEdge - (step - inputLocation.y))
        elif direction.symbol() == "E":
            return location.Location((inputLocation.x + step) % self.westEdge, inputLocation.y)
        elif direction.symbol() == "W":
            return location.Location(inputLocation.x > step: inputLocation.x - step else: self.westEdge - (step - inputLocation.x), inputLocation.y)