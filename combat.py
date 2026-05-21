from character import Enemy

def random_monster_encounter(player):
    enemy = Enemy("Goblin", 1, 0, 20)
    won_battle = None
    
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
        won_battle = True

    return won_battle
