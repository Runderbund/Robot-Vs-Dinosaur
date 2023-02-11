from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot("Marta")
        self.dinosaur = Dinosaur("Bob", 15)
        
    
    def run_game(self):
        self.display_welcome()
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.battle_phase() # Not defined # Wasn't indented or self.
        self.display_winner()

    def display_welcome(self):
        print ("Welcome to the battlefield!\n") 

    def battle_phase(self):
        #Make random start late
        # This is a clunky way to do it, but I don't think I'd separate display_welcome
        # battle_phase and run_game to start with.
        self.robot.attack(self.dinosaur)
        if self.dinosaur.health > 0:
            self.dinosaur.attack(self.robot)

    def display_winner(self):
        winner, loser = self.dinosaur.name, self.robot.name
        if self.robot.health > self.dinosaur.health:
             winner, loser = self.robot.name, self.dinosaur.name
        print (f"{winner} made {loser} extinct!")
        print (f"{winner} wins!")