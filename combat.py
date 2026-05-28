"""Functions related to combat"""
from town import inventory_management
import character
import random as rand

def choose_random_monster(player) -> character.Character:
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

def random_monster_encounter(player, enemy) -> bool:
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
        won_battle = False
    else:
        print("You are victorious!")
        enemy.defeat_and_loot_character(player)
        won_battle = True

    return won_battle

def player_combat_action(player, enemy) -> None:
    """Defines what the player can do during combat"""
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
    Armor Aware: Uses Armor Piercing Strike if the player's armor blocks half or more of their damage and they are at max stamina. 
    Complex: Willing to use all of their stamina. Uses Armor Piercing Strike if armor blocks half or more damage, otherwise uses Double Strike.
    """
    if enemy.combat_strategy == "Simple":
        enemy.weapon.attack(enemy, player)
    elif enemy.combat_strategy == "Cautious Double Strike":
        if enemy.stamina == enemy.max_stamina:
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

