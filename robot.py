from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Eye-lasers", 12)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print (f"{self.name} attacks {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage.")
        print (f"{dinosaur.name} has {max(dinosaur.health, 0)} health remaining.\n")
        # Bonus: Choose from List of 3 weapons before each attack