from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.robot = Robot("Marta")
        self.dinosaur = Dinosaur("Bob")
    
    def run_game(self):
        self.display_welcome()
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print ("Welcome to the battlefield!\n") 

    def battle_phase(self):
        self.robot.attack(self.dinosaur)
        if self.dinosaur.health > 0:
            self.dinosaur.attack(self.robot)

    def display_winner(self):
        winner, loser = self.dinosaur, self.robot
        if self.robot.health > self.dinosaur.health:
             winner, loser = self.robot, self.dinosaur
        print (f"{winner.name} made {loser.name} extinct!")
        print (f"{winner.name} wins!")