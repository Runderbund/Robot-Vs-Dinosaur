from weapon import Weapon
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 150) #Provides variability from run to run  
        self.choose_weapon()

    def attack(self, dinosaur):
        self.choose_weapon()
        dinosaur.health -= self.active_weapon.attack_power
        print (f"Robot {self.name} attacks {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} damage.")
        print (f"{dinosaur.name} has {max(dinosaur.health, 0)} health remaining.\n")
    
    def choose_weapon(self):
        #Each attack, a random weapon is used
        weapon_list = [Weapon("Eye-lasers", 12), Weapon("Sword", 10), Weapon("Shuriken", 5)]
        self.active_weapon = weapon_list[random.randint(0,2)]