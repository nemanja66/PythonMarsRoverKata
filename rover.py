from location import Location
from directions import NorthDirection 
from option import Result, Ok, Err

class Rover():
    def __init__(self, navigation):
        self.location = Location(0,0)
        self.direction = NorthDirection(self)
        self.navigation = navigation
        self.step = 1

    def execute(self, commands):
        if not commands:
            return self.format_output(self.location, self.direction)

        for c in commands:
            if c == 'M': 
                result_location = self.navigation.next_location_for(self.location, self.direction, self.step)
                if result_location.is_err:
                    return "O:" + self.format_output(result_location.unwrap_err(), self.direction)
                else: 
                    self.location = result_location.unwrap()
            elif c in ['R', 'L']:
                self.direction.rotate(c)

        return self.format_output(self.location, self.direction)

    def format_output(self, location, direction):
        return f'{location.x}:{location.y}:{direction.symbol}'
        
        