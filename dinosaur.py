class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100 # Make random later
    
    def attack(self, robot):
        robot.health -= self.attack_power
        print (f"{self.name} attacks {robot.name} with for {self.attack_power} damage.")
        print (f"{robot.name} has {max(robot.health, 0)} health remaining.\n")