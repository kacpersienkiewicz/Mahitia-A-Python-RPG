import character
import weapons
import apparel
import combat

import random as rand

INITIAL_COINS: int = 100
INITIAL_LEVEL: int = 1
INITIAL_XP: int = 0
INITIAL_HEALTH: int = 100
INITIAL_HEALTH_MULT: int = 10
INITIAL_STAMINA: int = 100
INITIAL_STAMINA_MULT: int = 10

def enter_the_inn(player):
    while True:
        choice = str(input("You enter the Ivory Inn. The innkeeper, Jane, greets you. What would you like to do?\n\t1.Speak with Jane\n\t2.Grab a room to rest (10 coins)\n"))
        if choice == '1':
            print("You greet Jane")
            break
        elif choice == '2':
            choice = str(input(f"Resting at the inn costs 10 coins. You have {player.coins} coins. Would you like to continue?[y/n]\n"))
            if choice == 'y':
                rest_inn(player)
                break
            if choice == 'n':
                print("You decide to not rent a bed at the inn.")
                continue
            else:
                print("Only 'y' or 'n' are valid inputs. Please type one of those.")
                continue
        else:
            print(f"{choice} is not a valid choice. Please type in 1 or 2.")
            continue
    return

def rest_inn(player):
    print(f"You heal to {player.max_health} health from {player.health} health.")
    player.health = player.max_health
    print(f"You heal to {player.max_stamina} stamina from {player.stamina} stamina.")
    player.stamina = player.max_stamina

def go_to_the_market(player):
    left_shop = False # Remove if left_shop is deprecated
    choice = str(input("You go to the general store. Ingvar has a variety of weapons, and armor for sale. What would you like to buy:\n\t1. Weapons\n\t2. Armor\n\t3. Leave the shop\n"))
    while True:
        if choice == '1':
            # I think this can be put into a function so it can be reused for the weapon and apparel branches.
            print(f"Index\tName\t\tDamage\tDamage Type\tPrice")
            for index, value in enumerate(weapons.purchasable_weapons):
                print(f"{index}\t{value.name}\t{value.damage}\t{value.damage_type}\t{value.value}")
            while True:
                choice = str(input(f"Please enter the Index value of the item you want to buy. Enter '-1' to browse another set of items.\n"))
                if choice == '-1':
                    left_shop = True # Remove if left_shop is deprecated
                    break
                else:
                    try:
                        weapon_index = int(choice)
                        purchased_weapon =  weapons.purchasable_weapons[weapon_index]
                        if weapon_index < len(weapons.purchasable_weapons):
                            if player.coins >= purchased_weapon.value:
                                player.coins -= purchased_weapon.value
                                player.add_to_inventory(purchased_weapon)
                                while True:
                                    choice = str(input(f"You spend {purchased_weapon.value} coins to purchase the {purchased_weapon.name}. Would you like to equip it? [y/n]?\n"))
                                    if choice =='y':
                                        player.equip_weapon(purchased_weapon)
                                        left_shop = True # Necessary to not trigger the else statement in an infinite loop (else: print(f"{choice} is not a valid choice. Please type in 1, 2, or 3.") continue  )
                                        break
                                    elif choice == 'n':
                                        left_shop = True # Remove if left_shop is deprecated
                                        break
                                    else:
                                        print("Only 'y' or 'n' are valid inputs. Please enter one of those.")
                                        continue
                                break
                            else:
                                print(f"You cannot afford the {purchased_weapon.name} as you only have {player.coins} and it costs {purchased_weapon.value} coins.")
                                continue
                        else:
                            print("Please enter a valid index.")
                            continue                       
                    except ValueError:
                        print("Please enter a valid index.")
                        continue
        elif choice == '2':
            # I think this can be put into a function so it can be reused for the weapon and apparel branches.
            print(f"Index\tName\t\tArmor\tPrice")
            for key, value in enumerate(apparel.purchasable_apparel):
                print(f"{key}\t{value.name}\t{value.armor}\t{value.value}")
            while True:
                choice = str(input(f"Please enter the Index value of the item you want to buy. Enter '-1' to browse another set of items.\n"))
                if choice == '-1':
                    left_shop = True # Remove if left_shop is deprecated
                    break
                else:
                    try:
                        apparel_index = int(choice)
                        purchased_apparel =  apparel.purchasable_apparel[apparel_index]
                        if apparel_index < len(apparel.purchasable_apparel):
                            if player.coins >= purchased_apparel.value:
                                player.coins -= purchased_apparel.value
                                player.add_to_inventory(purchased_apparel)
                                while True:
                                    choice = str(input(f"You spend {purchased_apparel.value} coins to purchase the {purchased_apparel.name}. Would you like to equip it? [y/n]?\n"))
                                    if choice =='y':
                                        player.equip_apparel(purchased_apparel)
                                        left_shop = True # Necessary to not trigger the else statement in an infinite loop (else: print(f"{choice} is not a valid choice. Please type in 1, 2, or 3.") continue  )
                                        break
                                    elif choice == 'n':
                                        left_shop = True # Remove if left_shop is deprecated
                                        break
                                    else:
                                        print("Only 'y' or 'n' are valid inputs. Please enter one of those.")
                                        continue
                                break
                            else:
                                print(f"You cannot afford the {purchased_apparel.name} as you only have {player.coins} and it costs {purchased_apparel.value} coins.")
                                continue
                        else:
                            print("Please enter a valid index.")
                            continue                       
                    except ValueError:
                        print("Please enter a valid index.")
                        continue
        elif choice =='3' or left_shop == True:
            break
        else:
            print(f"{choice} is not a valid choice. Please type in 1, 2, or 3.")
            continue           
    return

def main():
    name = str(input("What is your name?\n"))
    Hero = character.Player(name, INITIAL_LEVEL, INITIAL_XP, INITIAL_COINS, INITIAL_HEALTH,INITIAL_HEALTH_MULT, INITIAL_STAMINA, INITIAL_STAMINA_MULT, weapons.copper_sword, apparel.leather_armor)
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