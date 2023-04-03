from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.robot_health = 100
        self.robot_active_weapons = Weapon('Big-O-Gun', 30)

    def robot_attack(self, dinosaur): # need logic, void
        self.robot_active_weapons = Weapon('Big-O-Gun', 30)
        dinosaur -= self.robot_active_weapons.weapon_attack_power #attacks dinosaur
        print(f'{self.robot_name} attacked {dinosaur} with {self.robot_active_weapons.weapon_name} for {self.robot_active_weapons.weapon_attack_power} damage!')
      
