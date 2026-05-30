import weapons
import apparel
import quest

def enter_the_inn(player) -> None:
    """Player enters the inn to rest."""
    while True:
        choice = input("You enter the Ivory Inn. The innkeeper, Jane, greets you. What would you like to do?\n\t1. Rest at the inn (10 coins)\n\t2. Speak with the Innkeeper\n\t3. Leave the Inn\n")
        if choice == '1':
            while True:
                choice = input("Resting at the inn costs 10 coins. Would you like to rest at the inn? [y/n]?\n")
                if choice == 'y':
                    rest_inn(player)
                    break
                elif choice == 'n':
                    print("You decide to not rent a bed at the inn.")
                    break
                else:
                    print("Only 'y' or 'n' are valid inputs. Please type one of those.")
            break
        if choice == '2':
            while True:
                choice = input("What do you want to ask Jane about?\n\t1. How long has she owned the inn?\n\t2. Anything happening around town?\n\t3. Leave the inn\n")
                if choice == '1':
                    print("I've owned this inn since five years ago, when I inherited it from my mother who established the place 30 years ago.\n")
                elif choice == '2':
                    response = "Scrimshaw has been busy lately, though not for the best reasons."
                    call_to_action = "Would you like to ask about any of these threads?"
                    if quest.quest_goblin_encampment.completed == False:
                        response += " A local goblin encampment is terrorizing the locals."
                        call_to_action += "\n\t1. Ask about the goblin encampment."
                    if quest.quest_forest_cleanup.completed == False:
                        response += " Wolves are attacking hunters are farmers alike."
                        call_to_action += "\n\t2. Ask about the wolves."
                    if quest.quest_bandit_lord_showdown == False and player.level >= 5:
                        response += " A bandit lord is challenging everyone in town."
                        call_to_action += "\n\t3. Ask about the bandit lord."
                    if quest.quest_dark_knights_fortress == False and player.level >= 10:
                        response += " A farmer found a massive castle belonging to Dark Knights."
                        call_to_action += "\n\t4. Ask about the Dark Knight's Fortress."
                    
                    call_to_action += "\n\t5. Leave the inn."

                    while True:
                        print(response)
                        choice = input(call_to_action)
                        if choice == '1':
                            quest_prompt = "There's a small group of goblins led by a better armed warrior. The town has raised a fund of 50 coins to get rid of them."
                            accept_reject_quest(player, quest_prompt, quest.quest_goblin_encampment)
                            break
                        if choice == '2':
                            quest_prompt = "Wolves have been harrassing hunters and farmers which is harming our livelihoods. There are rumors of a dire wolf among them. The town has raised a fund of 50 coins to get rid of the dire wolf."
                            accept_reject_quest(player, quest_prompt, quest.quest_forest_cleanup)
                            break
                        if choice == '3':
                            quest_prompt = "An obnoxious bandit lord has been boasting and insulting everyone. We are sick of him, and raised 100 coins to get rid of him."
                            accept_reject_quest(player, quest_prompt, quest.quest_bandit_lord_showdown)
                            break
                        if choice == '4':
                            quest_prompt = "Fred mentioned that he was picking mushrooms and found a castle made of blackened rock off in the forest. We're not happy about the revelation and raised 150 coins to get rid of it."
                            accept_reject_quest(player, quest_prompt, quest.quest_dark_knights_fortress)
                            break
                        if choice == '5':
                            break
                        else:
                            print(f"{choice} is not a valid choice. Please type in 1, 2, 3, 4 or 5.")
                    break
                elif choice == '3':
                    break
                else:
                    print(f"{choice} is not a valid choice. Please type in 1, 2, or 3.")
            break
        if choice == '3':
            break

def accept_reject_quest(player, quest_prompt: str, quest: quest.Quest) -> None:
    """Allows the player to reject or accept a quest."""
    while True:
        print(quest_prompt)
        choice = input("Do you accept this quest? [y/n]?\nNote that you will immediately undertake the quest, so prepare beforehand.\n")
        if choice == 'y':
            quest.quest_function(player)
            break
        elif choice == 'n':
            break
        else:
            print("Only 'y' or 'n' are valid inputs. Please enter one of those.")
            continue


def rest_inn(player) -> None:
    """Simply allows the player to restore health and stamina"""
    print(f"You heal to {player.max_health} health from {player.health} health.")
    player.health = player.max_health
    print(f"You heal to {player.max_stamina} stamina from {player.stamina} stamina.")
    player.stamina = player.max_stamina

def go_to_the_market(player) -> None:
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

def inventory_management(player) -> None:
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

def equip_item(player, item) -> None:
    """Equip an equippable item."""
    if isinstance(item, weapons.Weapon):
        player.equip_weapon(item)
    elif isinstance(item, apparel.Apparel):
        player.equip_apparel(item)
    else:
        print(f"Cannot equip item of type {type(item)}")
    return

def present_store_stock(stock) -> None:
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

def store_logic(player, stock) -> None:
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
                break
            else:
                print(f"You cannot afford the {purchased_item.name} as you only have {player.coins} and it costs {purchased_item.value} coins.")
