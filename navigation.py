from location import Location
from option import Result, Ok, Err

class Navigation():
    def __init__(self, grid):
        self.grid = grid

    def next_location_for(self, input_location, direction, step):
        if direction.symbol == "N":
            for s in range (step):
                input_location.y = input_location.y + 1
                location = Location(input_location.x, input_location.y % self.grid.northEdge)
                if self.grid.is_obstacle(location): return Err(location)
            return Ok(location)
        elif direction.symbol == "S":
            for s in range (step):
                input_location.y = input_location.y - 1 if input_location.y > 0 else self.grid.northEdge - 1
                location = Location(input_location.x, input_location.y)      
                if self.grid.is_obstacle(location): return Err(location)  
            return Ok(location)
        elif direction.symbol == "E":
            for s in range (step):
                input_location.x = input_location.x + 1
                location = Location(input_location.x % self.grid.westEdge, input_location.y)
                if self.grid.is_obstacle(location): return Err(location)
            return Ok(location)
        elif direction.symbol == "W":
            for s in range (step):
                input_location.x = input_location.x - 1 if input_location.x > 0 else self.grid.westEdge - 1
                location = Location(input_location.x, input_location.y)
                if self.grid.is_obstacle(location): return Err(location)
            return Ok(location)