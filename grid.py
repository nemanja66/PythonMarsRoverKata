class Grid():
    def __init__(self, obstacles):
        self.northEdge = 10
        self.westEdge = 10
        self.obstacles = obstacles

    def is_obstacle(self, location):
        return location in self.obstacles

        