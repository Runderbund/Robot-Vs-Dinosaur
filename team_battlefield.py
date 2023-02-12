from fleet import Fleet
from herd import Herd


class Team_Battlefield:
    def __init__(self):
        self.robo_fleet = Fleet()
        self.dino_herd = Herd()
    
    def run_game(self):
        self.display_welcome()
        while self.robot.health > 0 and self.dinosaur.health > 0: # Change to team members left
            self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print ("Welcome to the battlefield!\n") 

    def battle_phase(self): #Use this in herd battle method
        #Make random start later
        self.robot.attack(self.dinosaur)
        if self.dinosaur.health > 0:
            self.dinosaur.attack(self.robot)

    def display_winner(self): # Team members, again
        winner, loser = self.dinosaur.name, self.robot.name
        if self.robot.health > self.dinosaur.health:
             winner, loser = self.robot.name, self.dinosaur.name
        print (f"{winner} made {loser} extinct!")
        print (f"{winner} wins!")