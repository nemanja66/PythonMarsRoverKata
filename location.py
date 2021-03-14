class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other): 
        if not isinstance(other, Location):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.x, self.y))