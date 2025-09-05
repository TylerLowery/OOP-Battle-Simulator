from enemy import Enemy

class BabyElf(Enemy):
    def take_damage(self, damage):
        print("Why ARE YOU ATTACKING A BABY ELF! YOUR MONSTER!")
        return super().take_damage(damage)