import southDirection
import northDirection

class WestDirection():
    def __init__(self, rover):
        self._rover = rover

    def rotate(self, side):
        if side == 'L': self._rover.direction = southDirection.SouthDirection(self._rover)
        elif side == 'R': self._rover.direction = northDirection.NorthDirection(self._rover)

    def symbol(self): return "W"