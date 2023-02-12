import random

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 150)
        self.attack_power = random.randint(7, 11)
    
    def attack(self, robot):
        robot.health -= self.attack_power
        print (f"Dinosaur {self.name} attacks {robot.name} with for {self.attack_power} damage.")
        print (f"{robot.name} has {max(robot.health, 0)} health remaining.\n")