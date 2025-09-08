from enemy import Enemy
import random

class Brute(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = random.randint(15, 20)

    def attack(self):
        if self.health < 50:
            self.attack_power = 50
        elif self.health < 150:
            self.attack_power = 40
        elif self.health < 200:
            self.attack_power = 20
        return self.attack_power
        
    def Boss_crit_hit(self):
        return random.randint(1, 100)
