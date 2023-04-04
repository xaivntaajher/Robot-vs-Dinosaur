class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
    
    def dinosaur_attack(self, robot): # need logic, void
        robot.health -= self.attack_power #attacks robot health
        print(f'{self.name} attacked {robot.name} for {self.attack_power} damage!')
        
        


