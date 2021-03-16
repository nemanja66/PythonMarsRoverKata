from location import Location
from option import Result, Ok, Err

class Grid():
    def __init__(self, obstacles):
        self.northEdge = 10
        self.westEdge = 10
        self.obstacles = obstacles

    def next_location_for(self, input_location, direction, step):
        if direction.symbol == "N":
            for s in range (step):
                input_location.y = input_location.y + 1
                location = Location(input_location.x, input_location.y % self.northEdge)
                if self.is_obstacle(location): return Err(location)
            return Ok(location)
        elif direction.symbol == "S":
            for s in range (step):
                input_location.y = input_location.y - 1 if input_location.y > 0 else self.northEdge - 1
                location = Location(input_location.x, input_location.y)      
                if self.is_obstacle(location): return Err(location)  
            return Ok(location)
        elif direction.symbol == "E":
            for s in range (step):
                input_location.x = input_location.x + 1
                location = Location(input_location.x % self.westEdge, input_location.y)
                if self.is_obstacle(location): return Err(location)
            return Ok(location)
        elif direction.symbol == "W":
            for s in range (step):
                input_location.x = input_location.x - 1 if input_location.x > 0 else self.westEdge - 1
                location = Location(input_location.x, input_location.y)
                if self.is_obstacle(location): return Err(location)
            return Ok(location)

    def is_obstacle(self, location):
        return location in self.obstacles

        