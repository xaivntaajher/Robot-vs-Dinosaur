from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapons = Weapon('Big-O-Gun', 30)

    def robot_attack(self, dinosaur): # need logic, void
        dinosaur.health -= self.active_weapons.attack_power #attacks dinosaur health
        print(f'{self.name} attacked {dinosaur.name} with {self.active_weapons.name} for {self.active_weapons.attack_power} damage!')
      
