from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.robot_health = 100
        self.robot_active_weapons = Weapon('Big Gun', 20)

    def robot_attack(self, dinosaur):
        self.attack = dinosaur