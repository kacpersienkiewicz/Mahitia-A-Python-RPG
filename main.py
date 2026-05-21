import character
import weapons
import apparel
import combat

import random as rand

INITIAL_COINS = 0
INITIAL_LEVEL = 1
INITIAL_XP = 0
INITIAL_HEALTH = 100
INITIAL_HEALTH_MULT = 10

def rest_inn(player):
    print(f"You heal to {player.max_health} from {player.health}.")
    player.health = player.max_health

def enter_the_inn(player):
    while True:
        choice = str(input("You enter the Ivory Inn. The innkeeper, Jane, greets you. What would you like to do?\n\t1.Speak with Jane\n\t2.Grab a room to rest (10 coins)\n"))
        if choice == '1':
            print("You greet Jane")
        elif choice == '2':
            rest_inn(player)
        else:
            print(f"{choice} is not a valid choice. Please type in 1 or 2.")
            continue

def go_to_the_market(player):
    choice = str(input("You go to the market. Which store would you like to go to?\n\t1. Blacksmith\n\t2. Fletcher\n\t3. General Store\n"))
    while True:
        if choice == '1':
            print("You enter Ingvar's shop. You hear the forge roaring, and the clanking of metal on metal. Ingvar greets you and asks if you want to buy anything.")
            break
        elif choice == '2':
            print("Fletcher")
            break
        elif choice == '3':
            print("General Store")
            break
        else:
            print("Only 1, 2 or 3 are valid choices.")
    

def main():
    name = str(input("What is your name?\n"))
    Hero = character.Character(name, INITIAL_LEVEL, INITIAL_XP, INITIAL_COINS, INITIAL_HEALTH,INITIAL_HEALTH_MULT, weapons.copper_sword, apparel.leather_armor)
    print("You start at level 1, with 100 coins. You are also granted a Copper Sword and Leather Armor.\n")

    print("Welome to Mahitia!")
    print("You are in the town of Scrimshaw, a small town whose economy is based on farming and the ivory trade.")

    while True:

        choice = str(input("What would you like to do?\n\t1. Fight Monsters\n\t2. Enter the Inn\n\t3. Go to the market.\n"))

        if choice == '1':
            enemy = rand.choice(character.random_monster_list)
            won_battle = combat.random_monster_encounter(Hero, enemy)
            if won_battle == False:
                break
            else:
                continue
        elif choice == '2':
            enter_the_inn(Hero)
        elif choice == '3':
            go_to_the_market(Hero)
        else:
            print(f"{choice} is not a valid choice. Please type in 1, 2, or 3.")
            continue
    
    print(f"You have lost. You were level {Hero.level}, and had {Hero.coins} coins at death.")

if __name__ == "__main__":
    main()