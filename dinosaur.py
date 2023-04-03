class Dinosaur:
    def __init__(self, name, attack_power):
        self.dinosaur_name = name
        self.dinosaur_attack_power = attack_power
        self.dinosaur_health = 100
    
    def dinosaur_attack(self, robot): # need logic, void
        robot.robot_health -= self.dinosaur_attack_power #attacks robot
        print(f'{self.dinosaur_name} attacked {robot.robot_name} for {self.dinosaur_attack_power} damage!')
        
        


