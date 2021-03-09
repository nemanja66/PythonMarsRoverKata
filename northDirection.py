import westDirection
import eastDirection

class NorthDirection():
    def __init__(self, rover):
        self._rover = rover

    def rotate(self, side):
        if side == 'L': self._rover.direction = westDirection.WestDirection(self._rover)
        elif side == 'R': self._rover.direction = eastDirection.EastDirection(self._rover)

    def symbol(self): return "N"



 