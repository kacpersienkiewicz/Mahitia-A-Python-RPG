from weapons import fists
from apparel import rags

class Character:
    def __init__(self, name: str, level: int, xp: int, coins: int):
        self.name = name
        self.character_class = "Commoner"
        self.level = level
        self.xp = xp
        self.coins = coins
        self.weapon = fists
        self.apparel = rags
        self.armor = rags.armor

    def __str__(self):
        return f"{self.name} is a level {self.level} {self.character_class}."

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.damage = weapon.damage

    def equip_apparel(self, apparel):
        self.apparel = apparel
        self.armor = apparel.armor

    def attack(self, target):
        target,health -= (self.damage - target.armor)

class Enemy(Character):
    def __init__(self, name, level, xp, coins):
        super().__init__(name, level, xp, coins)
        self.character_class = "Enemy"
        self.health_mult = 0
        self.health = 10 + self.level * self.health_mult
        self.max_health = self.health
    
    def look_at_enemy(self):
        print(f"You see a {self.name}, dressed in {self.apparel}, wielding {self.weapon}.")

    def loot_enemy(self, player):
        print(f"You loot the {self.name} and find {self.coins} coins.")
        player.coins += self.coins