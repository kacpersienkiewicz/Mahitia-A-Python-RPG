import weapons
import apparel

def enter_the_inn(player):
    """Player enters the inn to rest."""
    while True:
        choice = input("You enter the Ivory Inn. The innkeeper, Jane, greets you. Would you like to grab a room to rest (10 coins)?[y/n]\n")
        if choice == 'y':
            rest_inn(player)
            break
        elif choice == 'n':
            print("You decide to not rent a bed at the inn.")
            continue
        else:
            print("Only 'y' or 'n' are valid inputs. Please type one of those.")

def rest_inn(player):
    """Simply allows the player to restore health and stamina"""
    print(f"You heal to {player.max_health} health from {player.health} health.")
    player.health = player.max_health
    print(f"You heal to {player.max_stamina} stamina from {player.stamina} stamina.")
    player.stamina = player.max_stamina

def go_to_the_market(player):
    """Allows the player to buy new armor or weapons from the store. It should add the bought item to their inventory and allow them to equip it."""
    left_shop = False # Remove if left_shop is deprecated
    choice = input("You go to the general store. Ingvar has a variety of weapons, and armor for sale. What would you like to buy:\n\t1. Weapons\n\t2. Armor\n\t3. Leave the shop\n")
    while True:
        if choice == '1':
            # I think this can be put into a function so it can be reused for the weapon and apparel branches.
            print(f"Index\tName\t\tDamage\tDamage Type\tPrice")
            for index, value in enumerate(weapons.purchasable_weapons):
                print(f"{index}\t{value.name}\t{value.damage}\t{value.damage_type}\t{value.value}")
            while True:
                choice = input(f"Please enter the Index value of the item you want to buy. Enter '-1' to browse another set of items.\n")
                if choice == '-1':
                    left_shop = True # Remove if left_shop is deprecated
                    break
                else:
                    try:
                        weapon_index = int(choice)
                        if weapon_index < len(weapons.purchasable_weapons):
                            purchased_weapon =  weapons.purchasable_weapons[weapon_index]
                            if player.coins >= purchased_weapon.value:
                                player.coins -= purchased_weapon.value
                                player.add_to_inventory(purchased_weapon)
                                while True:
                                    choice = input(f"You spend {purchased_weapon.value} coins to purchase the {purchased_weapon.name}. Would you like to equip it? [y/n]?\n")
                                    if choice =='y':
                                        player.equip_weapon(purchased_weapon)
                                        left_shop = True # Necessary to not trigger the else statement in an infinite loop (else: print(f"{choice} is not a valid choice. Please type in 1, 2, or 3.") continue  )
                                        break
                                    elif choice == 'n':
                                        left_shop = True # Remove if left_shop is deprecated
                                        break
                                    else:
                                        print("Only 'y' or 'n' are valid inputs. Please enter one of those.")
                                break
                            else:
                                print(f"You cannot afford the {purchased_weapon.name} as you only have {player.coins} and it costs {purchased_weapon.value} coins.")
                        else:
                            print("Please enter a valid index.")                       
                    except ValueError:
                        print("Please enter a valid index.")
        elif choice == '2':
            # I think this can be put into a function so it can be reused for the weapon and apparel branches.
            print(f"Index\tName\t\tArmor\tPrice")
            for key, value in enumerate(apparel.purchasable_apparel):
                print(f"{key}\t{value.name}\t{value.armor}\t{value.value}")
            while True:
                choice = input(f"Please enter the Index value of the item you want to buy. Enter '-1' to browse another set of items.\n")
                if choice == '-1':
                    left_shop = True # Remove if left_shop is deprecated
                    break
                else:
                    try:
                        apparel_index = int(choice)
                        if apparel_index < len(apparel.purchasable_apparel):
                            purchased_apparel =  apparel.purchasable_apparel[apparel_index]
                            if player.coins >= purchased_apparel.value:
                                player.coins -= purchased_apparel.value
                                player.add_to_inventory(purchased_apparel)
                                while True:
                                    choice = input(f"You spend {purchased_apparel.value} coins to purchase the {purchased_apparel.name}. Would you like to equip it? [y/n]?\n")
                                    if choice =='y':
                                        player.equip_apparel(purchased_apparel)
                                        left_shop = True # Necessary to not trigger the else statement in an infinite loop (else: print(f"{choice} is not a valid choice. Please type in 1, 2, or 3.") continue  )
                                        break
                                    elif choice == 'n':
                                        left_shop = True # Remove if left_shop is deprecated
                                        break
                                    else:
                                        print("Only 'y' or 'n' are valid inputs. Please enter one of those.")
                                break
                            else:
                                print(f"You cannot afford the {purchased_apparel.name} as you only have {player.coins} and it costs {purchased_apparel.value} coins.")
                        else:
                            print("Please enter a valid index.")                       
                    except ValueError:
                        print("Please enter a valid index.")

        elif choice =='3' or left_shop == True:
            break
        else:
            print(f"{choice} is not a valid choice. Please type in 1, 2, or 3.")           

def inventory_management(player):
    """Allows the player to equip a different weapon or piece of armor. """

    while True:
        print(f"Your inventory is:\n")
        for i, item in enumerate(player.inventory):
            print(f"{i}\t{item}")
        print(f"You are currently wearing the {player.apparel.name} and are wielding the {player.weapon.name}.")
        choice = input("Would you like equip any of these items? Enter the item's index to equip it, or enter '-1' to stop managing your inventory.\n")

        try:
            inventory_index = int(choice)
        except ValueError:
            print("Please enter a valid index.")
            continue

        if inventory_index == -1:
            break
        elif inventory_index < len(player.inventory):
            selected_item = player.inventory[inventory_index]
            if type(selected_item) == type(weapons.purchasable_weapons[0]):
                player.equip_weapon(selected_item)
                print(f"You wield the {selected_item}.")
                break
            if type(selected_item) == type(apparel.purchasable_apparel[0]):
                player.equip_apparel(selected_item)
                print(f"You put on the {selected_item}.")
                break       
        else:
            print("Please enter a valid index.")
            continue