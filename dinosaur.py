class Dinosaur:
    def __init__(self, name, attack_power):
        self.dinosaur_name = name
        self.dinosaur_attack_power = attack_power
        self.dinosaur_health = 100
    
    def dinosaur_attack(self, robot):
        self.attack = robot