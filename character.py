import weapons
import apparel

class Character:
    def __init__(self, name: str, level: int, xp: int, coins: int, health: int, health_mult: int, stamina: int, stamina_mult: int, weapon, apparel):
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

    def __str__(self):
        return f"{self.name} is a level {self.level} {self.character_class}."

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.damage = weapon.damage

    def equip_apparel(self, apparel):
        self.apparel = apparel
        self.armor = apparel.armor

    def attack(self, target):
        damage = self.damage - target.armor
        if damage < 0:
            damage = 0
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage, who now has {target.health} health left.")

    def look_at_character(self):
        print(f"You see a {self.name}, dressed in {self.apparel.name}, wielding {self.weapon.name}.")

    def defeat_and_loot_character(self, player):
        print(f"You defeated the {self.name} and gain {self.xp} experience.")
        player.xp += self.xp
        if player.xp >= 100:
            player.xp -= 100
            player.level += 1
            player.health += player.health_mult
            player.max_health += player.health_mult
            print(f"You gained a level! You are now level {player.level}.")

        print(f"You loot the {self.name} and find {self.coins} coins.")
        player.coins += self.coins

class Player(Character):
    def __init__(self, name, level, xp, coins, health, health_mult, stamina, stamina_mult, weapon, apparel):
        super().__init__(name, level, xp, coins, health, health_mult, stamina, stamina_mult, weapon, apparel)
        self.inventory = {weapon.name:weapon, apparel.name:apparel}
    
    def add_to_inventory(self, item):
        self.inventory[str(item.name)] = item
        print(f"{item} was added to your inventory")


######################################################################################################################## 
# Enemy Calculation Variables
########################################################################################################################
#
# Weak Enemy variables
weak_level = 0
weak_xp = 5
weak_coins = 3
weak_health = 10
weak_health_mult = 5
weak_stamina = 10
weak_stamina_mult = 5

# Moderate Enemy Variables

# Hard Enemy Variables

# Difficult Enemy Variables


############################################################################################################################
# End of Enemy Variables
############################################################################################################################

# Enemies
goblin = Character("Goblin", weak_level, weak_xp, weak_coins, weak_health, weak_health_mult, weak_stamina, weak_stamina_mult, weapons.fists, apparel.rags)
giant_rat = Character("Giant Rat", weak_level, weak_xp, weak_coins, weak_health, weak_health_mult, weak_stamina, weak_stamina_mult, weapons.claws, apparel.nothing)
bandit = Character("Bandit", weak_level, 2 * weak_xp, 2* weak_coins, 2 * weak_health, weak_health_mult, 2 * weak_stamina, weak_stamina_mult, weapons.copper_sword, apparel.rags)

weak_random_monster_list = [goblin, giant_rat, bandit]
moderate_random_monster_list = []
hard_random_monster_list = []