"""Functions related to combat"""
from town import inventory_management
import character
import random as rand

def defeat_logic(player) -> None:
    """Handles a player dropping to 0 health."""
    if player.health <= 0:
        print(f"You have lost. You were level {player.level}, and had  {player.xp} experience and {player.coins} coins at death.")
        quit()
    else:
        print("You actually didn't lose. Probably shouldn't be here.")

def choose_random_monster(player) -> character.Character:
    """Choose a random encounter, based on the player's level, from a list of lists of Character objects"""
    if player.level < 5:
        monster_list = rand.choice(character.monster_roster[:1])
        enemy = rand.choice(monster_list)
    elif player.level < 10:
        monster_list = rand.choice(character.monster_roster[:2])
        enemy = rand.choice(monster_list)    
    else:
        monster_list = rand.choice(character.monster_roster)
        enemy = rand.choice(monster_list)
    return enemy

def monster_encounter(player, enemy):
    """
    Simulates a battle between the player and an enemy.

    Args:
        player (Character class): the player character
        enemy (Character class): the player's opponent

    """
    enemy.look_at_character()
    enemy.health = enemy.max_health
    print("You enter combat with them.")
    
    while True:
        if player.health <= 0 or enemy.health <= 0:
            break

        player_combat_action(player, enemy)
        enemy_combat_action(player, enemy)

        player.stamina += player.stamina_mult
        if player.stamina > player.max_stamina:
            player.stamina = player.max_stamina
        enemy.stamina += enemy.stamina_mult
        if enemy.stamina > enemy.max_stamina:
            enemy.stamina = enemy.max_stamina

    if player.health <= 0:
        print("You have been defeated.")
        defeat_logic(player)

    else:
        print("You are victorious!")
        enemy.defeat_and_loot_character(player)


def player_combat_action(player, enemy) -> None:
    """
    Defines what the player can do during combat

    Args:
        player (Character class): the player character
        enemy (Character class): the player's opponent
    """

    while True:
        choice = input(f"What would you like to do?\n\t1. Standard Attack\n\t2. Double Strike (Costs 25 Stamina)\n\t3. Armor Piercing Strike (Costs {25 + 5 * enemy.armor} Stamina)\n\t4. Inventory Management\n\t5. Character Status\n")
        if choice == '1':
            player.weapon.attack(player, enemy)
            break
        elif choice == '2':
            if player.stamina < 25:
                print(f"You do not have the required stamina to use double strike. You need 25 stamina and you have {player.stamina} stamina.")
                continue
            else:
                player.weapon.double_strike(player, enemy)
            break
        elif choice == '3':
            stamina_cost = (25 + 5 * enemy.armor)
            if player.stamina < stamina_cost:
                print(f"You do not have the required stamina to use the armor piercing strike. You need {stamina_cost} stamina and you have {player.stamina} stamina.")
                continue
            else:
                player.weapon.armor_pierce(player, enemy)
            break

        elif choice == '4':
            inventory_management(player)
            continue
        elif choice == '5':
            print(f"You are at {player.health} health, {player.stamina} stamina, and are wearing {player.apparel.name} and wielding a {player.weapon.name}.")
            continue
        else:
            print(f"{choice} is not a valid choice. Please type in 1, 2, 3 or 4.")
            continue

def enemy_combat_action(player, enemy) -> None:
    """
    Defines enemy logic for combat
    Simple: only standard attack
    Cautious Double Strike: Uses Double Strike at max stamina
    Reckless Double Strike: Uses Double Strike as possible
    Armor Aware: Uses Armor Piercing Strike if the player's armor blocks half or more of their damage and they are at max stamina.
    Complex: Willing to use all of their stamina. Uses Armor Piercing Strike if armor blocks half or more damage, otherwise uses Double Strike.

    Args:
        player (Character class): the player character
        enemy (Character class): the player's opponent
    """
    
    if enemy.combat_strategy == "Simple":
        enemy.weapon.attack(enemy, player)
    elif enemy.combat_strategy == "Cautious Double Strike":
        if enemy.stamina == enemy.max_stamina:
            enemy.weapon.double_strike(enemy, player)
        else:
            enemy.weapon.attack(enemy, player)
    elif enemy.combat_strategy == "Reckless Double Strike":
        if enemy.stamina >= 25:
            enemy.weapon.double_strike(enemy, player)
        else:
            enemy.weapon.attack(enemy, player)           
    elif enemy.combat_strategy == "Armor Aware":
        blocked_damage_threshold = enemy.damage // 2
        if player.armor >= blocked_damage_threshold and enemy.stamina == enemy.max_stamina:
            enemy.weapon.armor_pierce(enemy, player)
        else:
            enemy.weapon.attack(enemy, player)      
    elif enemy.combat_strategy == "Complex":
        blocked_damage_threshold = enemy.damage // 2
        armor_pierce_stamina_cost = 25 + player.armor * 5
        if player.armor >= blocked_damage_threshold and enemy.stamina >= armor_pierce_stamina_cost:
            enemy.weapon.armor_pierce(enemy, player)
        elif enemy.stamina >= 25:
            enemy.weapon.double_strike(enemy, player)
        else:
            enemy.weapon.attack(enemy, player)
    else:
        print(f"{enemy.combat_strategy} is not a documented strategy.")

