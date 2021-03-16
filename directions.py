class EastDirection():
    def __init__(self, rover):
        self.rover = rover

    def rotate(self, side):
        if side == 'L': self.rover.direction = NorthDirection(self.rover)
        elif side == 'R': self.rover.direction = SouthDirection(self.rover)

    @property
    def symbol(self): 
        return "E"

class NorthDirection():
    def __init__(self, rover):
        self.rover = rover

    def rotate(self, side):
        if side == 'L': self.rover.direction = WestDirection(self.rover)
        elif side == 'R': self.rover.direction = EastDirection(self.rover)

    @property
    def symbol(self): 
        return "N"

class SouthDirection():
    def __init__(self, rover):
        self.rover = rover

    def rotate(self, side):
        if side == 'L': self.rover.direction = EastDirection(self.rover)
        elif side == 'R': self.rover.direction = WestDirection(self.rover)

    @property
    def symbol(self): 
        return "S"

class WestDirection():
    def __init__(self, rover):
        self.rover = rover

    def rotate(self, side):
        if side == 'L': self.rover.direction = SouthDirection(self.rover)
        elif side == 'R': self.rover.direction = NorthDirection(self.rover)

    @property
    def symbol(self): 
        return "W"