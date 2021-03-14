import location
import northDirection
from option import Result, Ok, Err

class Rover():
    def __init__(self, grid):
        self._location = location.Location(0,0)
        self.direction = northDirection.NorthDirection(self)
        self._grid = grid

    def execute(self, commands, step):
        if not commands:
            return self.formatOutput(self._location, self.direction)

        self.commandList = list(commands)

        for c in self.commandList:
            if c == 'M': 
                resultLocation = self._grid.nextLocationFor(self._location, self.direction, step)
                if resultLocation.is_err:
                    return "O:" + self.formatOutput(resultLocation.unwrap_err(), self.direction)
                else: 
                    self._location = resultLocation.unwrap()
            elif c == 'R' or c == 'L':
                self.direction.rotate(c)

        return self.formatOutput(self._location, self.direction)

    def formatOutput(self, location, direction):
        return str(location.x) + ":" + str(location.y) + ":" + direction.symbol()
        