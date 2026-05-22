"""Functions related to combat, questing or leveling (since leveling is dependent on combat and questing)."""
from town import inventory_management

# 10 levels
levels = [int(round(pow(x, 1.1))) for x in range(100, 1000, 100)] # TODO: Implement Levels

def random_monster_encounter(player, enemy):
    enemy.look_at_character()
    print("You enter combat with them.")
    
    while True:
        if player.health <= 0 or enemy.health <= 0:
            break

        player.attack(enemy)
        enemy.attack(player)

    if player.health <= 0:
        print("You were defeated.")
        won_battle = False
    else:
        print("You are victorious!")
        enemy.defeat_and_loot_character(player)
        won_battle = True

    return won_battle


def player_combat_action(player, enemy):
    """Defines what the player can do during combat"""
    choice = input(f"What would you like to do?\n\t1. Standard Attack\n\t2. Weapon Special Attack (Costs x Stamina)\n\t3. Inventory Management\n\t4. Character Status\n")
    while True:
        if choice == '1':
            player.attack(enemy)
        elif choice == '2':
            pass # TODO
        elif choice == '3':
            inventory_management(player)
        elif choice == '4':
            print(f"You are at {player.health} health, {player.stamina} stamina, and are wearing {player.apparel.name} and wielding a {player.weapon.name}.")
        else:
            print(f"{choice} is not a valid choice. Please type in 1, 2, 3 or 4.")  


def enemy_combat_action(player, enemy):
    """Defines enemy logic for combat"""
    pass