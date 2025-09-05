import random

class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 200
        self.attack_power = random.randint(15, 20)
        #TODO Set the hero's name.
        #TODO Set the hero's health. You might give the hero more health than a goblin.
        #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
    

    def strike(self):
        return random.randint(1, self.attack_power)
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
        # TODO Implement take_damage
        # TODO We should prevent health from going into the NEGATIVE
    
    def is_alive(self):
        return self.health > 0
    #TODO define is_alive

    def Hero_crit_hit(self):
        return random.randint(1, 100)
