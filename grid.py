import location

class Grid():
    def __init__(self, obstacles):
        self.minHeight = 0
        self.minWidth = 0
        self.maxHeight = 10
        self.maxWidth = 10
        self._obstacles = obstacles

    def nextLocationFor(self, inputLocation, direction, step):
        if direction.symbol() == "N":
            return location.Location(inputLocation.x, inputLocation.y + step)
        elif direction.symbol() == "S":
            return location.Location(inputLocation.x, inputLocation.y - step)
        elif direction.symbol() == "E":
            return location.Location(inputLocation.x + step, inputLocation.y)
        elif direction.symbol() == "W":
            return location.Location(inputLocation.x - step, inputLocation.y)