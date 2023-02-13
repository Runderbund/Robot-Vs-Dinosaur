from fleet import Fleet
from herd import Herd


class Team_Battlefield:
    #Creates a Fleet of 3 robots and a Herd of 3 dinosaurs
    def __init__(self):
        self.robo_fleet = Fleet()
        self.dino_herd = Herd()
    
    def run_game(self):
        self.display_welcome()
        #While there is at least one of each remaining, the first member of each will battle
        #check_robots/dinos_left() returns a binary of 0 (False) or 1+ (True) remaining
        while self.robo_fleet.check_robots_left() and self.dino_herd.check_dinos_left():
            self.battle_phase(self.robo_fleet.robots[0], self.dino_herd.dinos[0])
        self.display_winner()

    def display_welcome(self):
        print ("Welcome to the battlefield!\n") 

    def battle_phase(self, robot, dinosaur):
        # Battle phase lasts until one combatant is <= 0 health
        # For now, the robot always attacks first. The overall outcome is roughly 50/50 already.
        while robot.health > 0 and dinosaur.health > 0:
            robot.attack(dinosaur)
            if dinosaur.health <= 0:
                print (f"{robot.name} vanquished {dinosaur.name}!\n")
                #Removes the dino at the first index and moves the next one (if any) up
                self.dino_herd.remove_dino(0)
            else:
                dinosaur.attack(robot)
                if robot.health <= 0:
                    print (f"{dinosaur.name} vanquished {robot.name}!\n")
                    self.robo_fleet.remove_robot(0)

    def display_winner(self):
        winner, loser = self.robo_fleet, self.dino_herd
        #Assumes the fleet wins. If there are dinosaurs left, it corrects the winner
        if self.dino_herd.check_dinos_left():
             winner, loser = self.dino_herd, self.robo_fleet
        print (f"{winner.name} made {loser.name} extinct!")
        print (f"{winner.name} wins!")