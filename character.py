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

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.damage = weapon.damage

    def equip_apparel(self, apparel):
        self.apparel = apparel
        self.armor = apparel.armor

    def __str__(self):
        return f"{self.name} is a level {self.level} {self.character_class}."

class Warrior(Character):
    def __init__(self, name, level, xp):
        super().__init__(name, level, xp)
        self.character_class = "Warrior"
        self.health_mult = 8
        self.health: float = 100 + level * self.health_mult
        self.max_health = self.health

class Archer(Character):
    def __init__(self, name, level, xp):
        super().__init__(name, level, xp)
        self.character_class = "Archer"

class Enemy(Character):
    def __init__(self, name, level, xp, coins):
        super().__init__(name, level, xp, coins)
        self.character_class = "Goblin"
        self.health_mult = 0
        self.health = 10
        self.max_health = self.health