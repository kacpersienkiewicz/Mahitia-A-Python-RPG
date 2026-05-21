import character
import weapons
import apparel
import combat

INITIALCOINS = 100
INITIALLEVEL = 1
INITIALXP = 0

def rest_inn(entity_character):
    entity_character.health = entity_character.max_health

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

def main():
    name = str(input("What is your name?\n"))
    Hero = character.Character(name, INITIALLEVEL, INITIALXP, INITIALCOINS)
    print("You start at level 1, with 100 coins. You are also granted a Copper Sword and Leather Armor.\n")
    Hero.equip_weapon(weapons.copper_sword)
    Hero.equip_apparel(apparel.leather_armor)

    while True:
        print("Welome to Mahitia!")
        print("You are in the town of Scrimshaw, a small town whose economy is based on farming and the ivory trade.")
        choice = str(input("What would you like to do?\n\t1. Fight Monsters\n\t2. Enter the Inn\n\t3. Go to the market.\n"))

        if choice == '1':
            won_battle = None
            won_battle = combat.random_monster_encounter(Hero)
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