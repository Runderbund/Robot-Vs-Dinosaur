from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = [Robot("Daneel"), Robot("Giskard"), Robot("T-1000")]
        self.name = "The Fleet"
        # Could allow for user inputs later
    
    def check_robots_left(self):
        return len(self.robots) > 0
    
    def remove_robot(self, index):
        self.robots.pop(index)