class Weapon:
    def __init__(self, name, damage, damage_type, value):
        self.name = name
        self.damage = damage
        self.damage_type = damage_type
        self.value = value

    def __str__(self):
        return f"{self.name} is a weapon which does {self.damage} damage, and is worth {self.value} coins."

class Blade(Weapon):
    def __init__(self, name, damage, damage_type, value, weapon_type="Blade"):
        super().__init__(name, damage, damage_type, value)
        self.weapon_type = weapon_type
    
    def slash(self, wielder, target):
        pass

fists = Weapon("Fists", 1, "Bludgeoning", 0)
claws = Weapon("Claws", 2, "Slashing", 0)
stone_sword = Weapon("Stone Sword", 2, "Slashing", 5)
copper_sword = Weapon("Copper Sword", 3, "Slashing", 10)
bronze_sword = Weapon("Bronze Sword", 4, "Slashing", 20)
iron_sword = Weapon("Iron Sword", 5, "Slashing", 30)
steel_sword = Weapon("Steel Sword", 6, "Slashing", 40)

purchasable_weapons = [stone_sword, copper_sword, bronze_sword, iron_sword, steel_sword]
