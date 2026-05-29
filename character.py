"""Classes and Functions related to characters, including the player and enemies"""

import weapons
import apparel

class Character:
    def __init__(self, name: str, level: int, xp: int, coins: int, health: int, health_mult: int, stamina: int, stamina_mult: int, weapon, apparel, combat_strategy="Simple"):
        self.name = name
        self.level = level
        self.xp = xp
        self.coins = coins
        self.health_mult = health_mult
        self.health = health + self.level * self.health_mult
        self.max_health = self.health
        self.stamina_mult = stamina_mult
        self.stamina = stamina + self.level * self.stamina_mult
        self.max_stamina = self.stamina
        self.character_class = "Commoner"
        self.weapon = weapon
        self.damage = weapon.damage
        self.apparel = apparel
        self.armor = apparel.armor
        self.combat_strategy = combat_strategy

    def __str__(self):
        return f"{self.name} is a level {self.level} {self.character_class}. They are dressed in {self.apparel} and are wielding a {self.weapon}. They currently have {self.xp} experience and {self.coins} coins."

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.damage = weapon.damage

    def equip_apparel(self, apparel):
        self.apparel = apparel
        self.armor = apparel.armor

    def look_at_character(self):
        print(f"You see a {self.name}, dressed in {self.apparel.name}, wielding {self.weapon.name}.")

    def defeat_and_loot_character(self, player):
        print(f"You defeat the {self.name} and gain {self.xp} experience.")
        player.xp += self.xp
        leveling(player)

        print(f"You loot the {self.name} and find {self.coins} coins.")
        player.coins += self.coins

class Player(Character):
    def __init__(self, name, level, xp, coins, health, health_mult, stamina, stamina_mult, weapon, apparel):
        super().__init__(name, level, xp, coins, health, health_mult, stamina, stamina_mult, weapon, apparel)
        self.inventory = [weapon, apparel]
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} was added to your inventory")


######################################################################################################################## 
# Enemy Calculation Variables
########################################################################################################################

weak_level = 0
moderate_level = 3
hard_level = 5

weak_xp = 10
moderate_xp = 25
hard_xp = 50

weak_coins = 5
moderate_coins = 15
hard_coins = 25

weak_health = 10
moderate_health = 20
hard_health = 35

weak_health_mult = 5
moderate_health_mult= 10
hard_health_mult = 20

weak_stamina = 10
moderate_stamina = 25
hard_stamina = 50

weak_stamina_mult = 5
moderate_stamina_mult= 15
hard_stamina_mult = 25

############################################################################################################################
# End of Enemy Variables
############################################################################################################################

# Enemies

# Weak
goblin = Character("Goblin", weak_level, weak_xp, weak_coins, weak_health, weak_health_mult, weak_stamina, weak_stamina_mult, weapons.fists, apparel.rags)
goblin_warrior = Character("Goblin Warrior", weak_level, weak_xp, weak_coins, weak_health, weak_health_mult, weak_stamina, weak_stamina_mult, weapons.copper_sword, apparel.rags)
giant_rat = Character("Giant Rat", weak_level, weak_xp, weak_coins, weak_health, weak_health_mult, weak_stamina, weak_stamina_mult, weapons.claws, apparel.rags)
bandit = Character("Bandit", weak_level, 2 * weak_xp, 2 * weak_coins, 2 * weak_health, weak_health_mult, 3 * weak_stamina, 2 * weak_stamina_mult, weapons.copper_sword, apparel.rags, combat_strategy="Cautious Double Strike")
wolf = Character("Wolf", weak_level, weak_xp, weak_coins, 2 * weak_health, weak_health_mult, 3 * weak_stamina, 3 * weak_stamina_mult, weapons.claws, apparel.nothing, combat_strategy="Cautious Double Strike")
bear = Character("Bear", weak_level, moderate_xp, weak_coins, 3 * weak_health, weak_health_mult, 3 * weak_stamina, 2 *weak_stamina_mult, weapons.claws, apparel.nothing, combat_strategy="Cautious Double Strike")

# Moderate
rat_king = Character("Rat King", weak_level, moderate_xp, moderate_coins, 2 * moderate_health, moderate_health_mult, moderate_stamina, moderate_stamina_mult, weapons.claws, apparel.rags, combat_strategy="Cautious Double Strike")
bandit_highwayman = Character("Bandit", moderate_level, moderate_xp, moderate_coins, moderate_health, 2 * moderate_health_mult, weak_stamina, 2 * weak_stamina_mult, weapons.copper_sword, apparel.leather_armor, combat_strategy="Cautious Double Strike")
dark_squire = Character("Dark Squire", moderate_level, 2 * moderate_xp, 2 * moderate_coins, moderate_health, 2 * moderate_health_mult, weak_stamina, 2 * weak_stamina_mult, weapons.iron_sword, apparel.leather_armor, combat_strategy="Armor Aware")
goblin_captain = Character("Goblin Captain", moderate_level, moderate_xp, 2 * moderate_coins, weak_health, moderate_health_mult, weak_stamina, 2 * weak_stamina_mult, weapons.copper_sword, apparel.leather_armor, combat_strategy="Cautious Double Strike")
wolf_dire = Character("Dire Wolf", moderate_level, moderate_xp, moderate_coins, moderate_health, moderate_health_mult, moderate_stamina, 2 * moderate_stamina_mult, weapons.claws, apparel.rags, combat_strategy="Cautious Double Strike")
bear_dire = Character("Dire Bear", moderate_level, 2 * moderate_xp, moderate_coins, moderate_health, 2 * moderate_health_mult, moderate_stamina, 2 * moderate_stamina_mult, weapons.claws, apparel.rags, combat_strategy="Cautious Double Strike")

# Hard
dark_knight = Character("Dark Knight")
goblin_commander = Character("Goblin Commander")
bandit_lord = Character("Bandit Lord")


# Monster Lists
weak_random_monster_list = [goblin, goblin_warrior, giant_rat, bandit, wolf, bear]
moderate_random_monster_list = [rat_king, bandit_highwayman, dark_squire, goblin_captain, wolf_dire, bear_dire]
hard_random_monster_list = []

monster_roster = [weak_random_monster_list, moderate_random_monster_list, hard_random_monster_list]

############################################################################################################################
# Leveling
############################################################################################################################
# 10 levels
levels = [int(round(pow(x, 1.1))) for x in range(100, 1000, 100)]

def leveling(player):
    current_xp = player.xp
    current_level = player.level
    if current_level < len(levels):
        next_level_threshold = levels[current_level - 1]
        if current_xp >= next_level_threshold:
            player.level += 1
            player.health += player.health_mult
            player.max_health += player.health_mult
            player.stamina += player.stamina_mult
            player.max_stamina += player.stamina_mult
            print(f"You gain a level! You are now level {player.level}.")