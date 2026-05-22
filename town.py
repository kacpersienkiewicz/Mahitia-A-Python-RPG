from weapons import purchasable_weapons
from apparel import purchasable_apparel

def enter_the_inn(player):
    """Player enters the inn to rest."""
    while True:
        choice = str(input("You enter the Ivory Inn. The innkeeper, Jane, greets you. Would you like to grab a room to rest (10 coins)?[y/n]\n"))
        if choice == 'y':
            rest_inn(player)
            break
        if choice == 'n':
            print("You decide to not rent a bed at the inn.")
            continue
        else:
            print("Only 'y' or 'n' are valid inputs. Please type one of those.")
            continue
    return

def rest_inn(player):
    """Simply allows the player to restore health and stamina"""
    print(f"You heal to {player.max_health} health from {player.health} health.")
    player.health = player.max_health
    print(f"You heal to {player.max_stamina} stamina from {player.stamina} stamina.")
    player.stamina = player.max_stamina

def go_to_the_market(player):
    """Allows the player to buy new armor or weapons from the store. It should add the bought item to their inventory and allow them to equip it."""
    left_shop = False # Remove if left_shop is deprecated
    choice = str(input("You go to the general store. Ingvar has a variety of weapons, and armor for sale. What would you like to buy:\n\t1. Weapons\n\t2. Armor\n\t3. Leave the shop\n"))
    while True:
        if choice == '1':
            # I think this can be put into a function so it can be reused for the weapon and apparel branches.
            print(f"Index\tName\t\tDamage\tDamage Type\tPrice")
            for index, value in enumerate(purchasable_weapons):
                print(f"{index}\t{value.name}\t{value.damage}\t{value.damage_type}\t{value.value}")
            while True:
                choice = str(input(f"Please enter the Index value of the item you want to buy. Enter '-1' to browse another set of items.\n"))
                if choice == '-1':
                    left_shop = True # Remove if left_shop is deprecated
                    break
                else:
                    try:
                        weapon_index = int(choice)
                        purchased_weapon =  purchasable_weapons[weapon_index]
                        if weapon_index < len(purchasable_weapons):
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
            for key, value in enumerate(purchasable_apparel):
                print(f"{key}\t{value.name}\t{value.armor}\t{value.value}")
            while True:
                choice = str(input(f"Please enter the Index value of the item you want to buy. Enter '-1' to browse another set of items.\n"))
                if choice == '-1':
                    left_shop = True # Remove if left_shop is deprecated
                    break
                else:
                    try:
                        apparel_index = int(choice)
                        purchased_apparel =  purchasable_apparel[apparel_index]
                        if apparel_index < len(purchasable_apparel):
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