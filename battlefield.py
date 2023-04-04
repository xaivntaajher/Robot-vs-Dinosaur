from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot('Lazer')
        self.dinosaur = Dinosaur('Dino', 35)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.diplay_winner()

    def display_welcome(self):
        print('Welcome to the battle! Who will when this battle?')

    def battle_phase(self):       
        while self.robot.health > 0 and self.dinosaur.health > 0: 
            self.dinosaur.health >= self.robot.active_weapons.attack_power
            self.robot.robot_attack(self.dinosaur) # robot attack
            # self.dinosaur.dinosaur_health -= self.robot.robot_active_weapons.weapon_attack_power
            print(f'{self.dinosaur.name} has {self.dinosaur.health} hp remaining!')  
            self.robot.health >= self.dinosaur.attack_power
            self.dinosaur.dinosaur_attack(self.robot) # dinosaur attack
            # self.robot.robot_health -= self.dinosaur.dinosaur_attack_power
            print(f'{self.robot.name} has {self.robot.health} hp remaining!')        

    def diplay_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} wins the battle!')
            print(f'{self.robot.name} loses the battle!')
        elif self.dinosaur.health <= 0:
            print(f'{self.robot.name} wins the battle!')
            print(f'{self.dinosaur.name} loses the battle')
        
        