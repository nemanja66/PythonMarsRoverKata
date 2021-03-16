import location
from directions import NorthDirection 
from option import Result, Ok, Err

class Rover():
    def __init__(self, grid):
        self._location = location.Location(0,0)
        self.direction = NorthDirection(self)
        self._grid = grid

    def execute(self, commands, step):
        if not commands:
            return self.formatOutput(self._location, self.direction)

        for c in commands:
            if c == 'M': 
                resultLocation = self._grid.nextLocationFor(self._location, self.direction, step)
                if resultLocation.is_err:
                    return "O:" + self.formatOutput(resultLocation.unwrap_err(), self.direction)
                else: 
                    self._location = resultLocation.unwrap()
            elif c in ['R', 'L']:
                self.direction.rotate(c)

        return self.formatOutput(self._location, self.direction)

    def formatOutput(self, location, direction):
        return str(location.x) + ":" + str(location.y) + ":" + direction.symbol
        