class EastDirection():
    def __init__(self, rover):
        self._rover = rover

    def rotate(self, side):
        if side == 'L': self._rover.direction = NorthDirection(self._rover)
        elif side == 'R': self._rover.direction = SouthDirection(self._rover)

    def symbol(self): return "E"

class NorthDirection():
    def __init__(self, rover):
        self._rover = rover

    def rotate(self, side):
        if side == 'L': self._rover.direction = WestDirection(self._rover)
        elif side == 'R': self._rover.direction = EastDirection(self._rover)

    def symbol(self): return "N"

class SouthDirection():
    def __init__(self, rover):
        self._rover = rover

    def rotate(self, side):
        if side == 'L': self._rover.direction = EastDirection(self._rover)
        elif side == 'R': self._rover.direction = WestDirection(self._rover)

    def symbol(self): return "S"

class WestDirection():
    def __init__(self, rover):
        self._rover = rover

    def rotate(self, side):
        if side == 'L': self._rover.direction = SouthDirection(self._rover)
        elif side == 'R': self._rover.direction = NorthDirection(self._rover)

    def symbol(self): return "W"