import character
import weapons
import apparel
import combat
import town

import random as rand

INITIAL_COINS: int = 100
INITIAL_LEVEL: int = 1
INITIAL_XP: int = 0
INITIAL_HEALTH: int = 100
INITIAL_HEALTH_MULT: int = 10
INITIAL_STAMINA: int = 100
INITIAL_STAMINA_MULT: int = 10

def main():
    Hero = character.Player("Hero", INITIAL_LEVEL, INITIAL_XP, INITIAL_COINS, INITIAL_HEALTH,INITIAL_HEALTH_MULT, INITIAL_STAMINA, INITIAL_STAMINA_MULT, weapons.copper_sword, apparel.leather_armor)
    print(f"You start at level {INITIAL_LEVEL}, with {INITIAL_COINS} coins. You are also granted a Copper Sword and Leather Armor.\n")

    print("Welome to Mahitia!")
    print("You are in the town of Scrimshaw, a small town whose economy is based on farming and the ivory trade.")

    while True:

        choice = input("What would you like to do?\n\t1. Fight Monsters\n\t2. Rest at the Inn\n\t3. Buy Weapons/Armor\n\t4. Manage Inventory\n")

        if choice == '1':
            enemy = rand.choice(character.weak_monster_list)
            won_battle = combat.random_monster_encounter(Hero, enemy)
            if won_battle == False:
                break
            else:
                continue
        elif choice == '2':
            town.enter_the_inn(Hero)
        elif choice == '3':
            town.go_to_the_market(Hero)
        elif choice =='4':
            town.inventory_management(Hero)
        else:
            print(f"{choice} is not a valid choice. Please type in 1, 2, 3 or 4.")
            continue
    
    print(f"You have lost. You were level {Hero.level}, and had {Hero.coins} coins at death.")

if __name__ == "__main__":
    main()