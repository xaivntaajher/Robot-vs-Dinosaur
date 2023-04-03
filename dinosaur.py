class Dinosaur:
    def __init__(self, name, attack_power):
        self.dinosaur_name = name
        self.dinosaur_attack_power = attack_power
        self.dinosaur_health = 100
    
    def dinosaur_attack(self, robot): # need logic, void
        self.dinosaur_attack_power = 30
        if self.dinosaur_attack_power <= robot:
            self.dinosaur_attack_power -= robot #attacks robot
            print(f'{self.dinosaur_name} attacked {robot} for {self.dinosaur_attack_power} damage!')
        
        


