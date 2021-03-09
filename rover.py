import coordinates
import northDirection

class Rover():
    def __init__(self):
        self._coordinates = coordinates.Coordinates(1,1)
        self.direction = northDirection.NorthDirection(self)

    def execute(self, commands):
        if not commands:
            return self.formatOutput(self._coordinates, self.direction)

        self.commandList = list(commands)

        for c in self.commandList:
            if c == 'R': 
                self.direction.rotate(c)
            elif c == 'M': 
                self._coordinates.y = self._coordinates.y + 1

        return self.formatOutput(self._coordinates, self.direction)

    def formatOutput(self, coordinates, direction):
        return str(coordinates.x) + ":" + str(coordinates.y) + ":" + direction.symbol()
        