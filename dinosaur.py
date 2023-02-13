import random

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 150)
        self.attack_power = random.randint(7, 11) #Provides variability from run to run
    
    def attack(self, robot):
        attack_power = self.attack_power+random.randint(-2, 2) #Provides variability from attack to attack
        robot.health -= attack_power
            #Could instead check max(robot.health, 0) here and set robot health to 0 exactly.
        print (f"Dinosaur {self.name} attacks {robot.name} with for {attack_power} damage.")
        print (f"{robot.name} has {max(robot.health, 0)} health remaining.\n")