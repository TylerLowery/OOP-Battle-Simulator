import random
from goblin import Goblin
from hero import Hero
<<<<<<< Updated upstream
=======
from boss import Brute
>>>>>>> Stashed changes

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
<<<<<<< Updated upstream
    hero = Hero("Aragorn")
=======
    hero = Hero("Mr Speak")
>>>>>>> Stashed changes

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
<<<<<<< Updated upstream
=======
    total_damage = 0
    rounds = 0
    Criticals_hits = 0
    Miss_attack = 0
    boss_critical_hits = 0
    Boss_Rounds = 0
>>>>>>> Stashed changes

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    if hero.is_alive():
        print("Boss Time!!!")
        MR_SPEAK = Brute(" EVIL MR SPEAK")
        while hero.is_alive() and MR_SPEAK.is_alive():
            print("\nNew Round!")
            Boss_Rounds +=1
            damage = hero.strike()
            if hero.Hero_crit_hit() > 74:
                damage += 25
                Criticals_hits += 1
            if hero.Hero_crit_hit() < 26:
                damage = 0
                Miss_attack += 1
            MR_SPEAK.take_damage(damage)

            damage = MR_SPEAK.attack()
            if MR_SPEAK.Boss_crit_hit() > 74:
                damage += 25
                boss_critical_hits += 1
            hero.receive_damage(damage)
        if hero.is_alive():
            print(f"\nThe hero has defeated the BOSS!! ༼ ᕤ◕◡◕ ༽ᕤ")
        else:
            print(f"\nThe boss defeated the hero Game Over. (｡•́︿•̀｡)")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
<<<<<<< Updated upstream
=======
    print(f"total damage dealt " + str(total_damage))
    print(f"round " + str(rounds))
    print(f"critical hits landed " + str(Criticals_hits))
    print(f"Missed Attacks " + str (Miss_attack))
    print(f"Boss Rounds " + str(Boss_Rounds))
    print(f"Boss Critical Hits " + str(boss_critical_hits))
>>>>>>> Stashed changes

if __name__ == "__main__":
    main()
