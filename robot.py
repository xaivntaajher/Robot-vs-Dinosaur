from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.robot_health = 100
        self.robot_active_weapons = Weapon()

    def robot_attack(self, dinosaur): # need logic, void
        self.robot_active_weapons -= Weapon([2])
        print(f'{self.robot_name} attacked {dinosaur} with {Weapon([0])} for {Weapon([1])} damage!')
        print(f'{dinosaur} has')


