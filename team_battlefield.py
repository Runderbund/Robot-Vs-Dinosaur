from fleet import Fleet
from herd import Herd


class Team_Battlefield:
    def __init__(self):
        self.robo_fleet = Fleet()
        self.dino_herd = Herd()
    
    def run_game(self):
        self.display_welcome()
        while self.robo_fleet.check_robots_left() and self.dino_herd.check_dinos_left():
            self.battle_phase(self.robo_fleet.robots[0], self.dino_herd.dinos[0])
        self.display_winner()

    def display_welcome(self):
        print ("Welcome to the battlefield!\n") 

    def battle_phase(self, robot, dinosaur): #Use this in herd battle method
        #Make random start later
        while robot.health > 0 and dinosaur.health > 0:
            robot.attack(dinosaur)
            if dinosaur.health > 0:
                dinosaur.attack(robot)
        if robot.health <= 0:
            self.robo_fleet.remove_robot(0)
        else:
            self.dino_herd.remove_dino(0)

    def display_winner(self): # Team members, again
        winner, loser = self.robo_fleet.name, self.dino_herd.name
        if self.dino_herd.check_dinos_left():
             winner, loser = self.dino_herd.name, self.robo_fleet.name
        print (f"{winner} made {loser} extinct!")
        print (f"{winner} wins!")
    
    # def start_team_battle(self):
    #     combatants_remain = check_robots_left() and 
    #     pass