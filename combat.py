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
    pass

def enemy_combat_action(player, enemy):
    """Defines enemy logic for combat"""
    pass