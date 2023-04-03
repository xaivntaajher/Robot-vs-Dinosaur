from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot('Lazer')
        self.dinosaur = Dinosaur('Dino', 30)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.diplay_winner()

    def display_welcome(self):
        print('Welcome to the battle! Who will when this battle?')

    def battle_phase(self):
        while self.robot.robot_health > 0 and self.dinosaur.dinosaur_health > 0:
            if self.dinosaur.dinosaur_health > 0:
                self.robot.robot_attack('Dino')                
                print(f'{self.dinosaur.dinosaur_name} has {self.dinosaur.dinosaur_health} remaining!')
            elif self.robot.robot_health > 0:
                self.dinosaur.dinosaur_attack('Lazer')
                print(f'{self.robot.robot_name} has {self.robot.robot_health} remaining!')
            
    def diplay_winner(self):
        if self.robot.robot_health <= 0:
            print(f'{self.dinosaur.dinosaur_name} wins the battle!')
        elif self.dinosaur.dinosaur_health <= 0:
            print(f'{self.robot.robot_name} wins the battle!')
        print('The End')
        