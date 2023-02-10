class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def attack(self, robot):
        robot.health -= self.attack_power
        print (f"{self.name} attacks {robot.name}  with {self.active_weapon} for {self.attack_power} damage.")
        print (f"{robot.name} has {robot.health} health remaining.")
        # Lower robot health by dino att power
        # 6 lines
        pass