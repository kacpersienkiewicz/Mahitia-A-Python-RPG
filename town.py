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
    choice = input("You go to the general store. Ingvar has a variety of weapons, and armor for sale. What would you like to buy:\n\t1. Weapons\n\t2. Armor\n\t3. Leave the shop\n")
    while True:
        if choice == '1':
            store_logic(player, weapons.purchasable_weapons)
            break
        elif choice == '2':
            store_logic(player, apparel.purchasable_apparel)
            break
        elif choice =='3':
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

def equip_item(player, item):
    """Equip an equippable item."""
    if isinstance(item, weapons.Weapon):
        player.equip_weapon(item)
    elif isinstance(item, apparel.Apparel):
        player.equip_apparel(item)
    else:
        print(f"Cannot equip item of type {type(item)}")
    return

def present_store_stock(stock):
    """Prints out the store's stock in a tabular fashion"""
    if isinstance(stock[0], weapons.Weapon):
        print(f"Index\tName\t\tDamage\tDamage Type\tPrice")
        for index, value in enumerate(stock):
            print(f"{index}\t{value.name}\t{value.damage}\t{value.damage_type}\t{value.value}")
    elif isinstance(stock[0], apparel.Apparel):
        print(f"Index\tName\t\tArmor\tPrice")
        for key, value in enumerate(apparel.purchasable_apparel):
            print(f"{key}\t{value.name}\t{value.armor}\t{value.value}")
    else:
        print(f"{type(stock[0])} is an invalid type for presenting store stock.")
    return

def store_logic(player, stock):
    """Takes in a store's stock, the player's info and figures out the logic for the store so the player can buy stuff."""
    while True:
        present_store_stock(stock)
        choice = input(f"Please enter the Index value of the item you want to buy. Enter '-1' to leave the market.\n")
        try:
            stock_index = int(choice)
        except ValueError:
            print("Please enter a valid index.")
            continue
        
        if stock_index == -1:
            break
        elif stock_index < len(stock):
            purchased_item = stock[stock_index]
            if player.coins >= purchased_item.value:
                player.coins -= purchased_item.value
                player.add_to_inventory(purchased_item)
                while True:
                    choice = input(f"You spend {purchased_item.value} coins to purchase the {purchased_item.name}. Would you like to equip it? [y/n]?\n")
                    if choice == 'y':
                        equip_item(player, purchased_item)
                        break
                    elif choice == 'n':
                        break
                    else:
                        print("Only 'y' or 'n' are valid inputs. Please enter one of those.")
                        continue
            else:
                print(f"You cannot afford the {purchased_item.name} as you only have {player.coins} and it costs {purchased_item.value} coins.")
