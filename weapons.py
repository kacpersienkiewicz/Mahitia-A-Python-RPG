class Weapon:
    def __init__(self, name, damage, weapon_type, material, value):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type
        self.material = material
        self.value = value

    def __str__(self):
        if self.material == None:
            return f"{self.name} is a(n) {self.weapon_type} weapon which does {self.damage} damage, and is worth {self.value} coins."
        else:
            return f"{self.name} is a(n) {self.material} {self.weapon_type} weapon which does {self.damage} damage, and is worth {self.value} coins."

    def attack(self, target) -> None:
        target.health -= (self.damage - target.armor)


fists = Weapon("Fists", 1, "Unarmed", None, 0)
claws = Weapon("Claws", 2, "Unarmed", None, 0)
stone_sword = Weapon("Stone Sword", 2, "Blade", "Stone", 5)
copper_sword = Weapon("Copper Sword", 3, "Blade", "Copper", 10)
bronze_sword = Weapon("Bronze Sword", 4, "Blade", "Bronze", 20)
iron_sword = Weapon("Iron Sword", 5, "Blade", "Iron", 30)
steel_sword = Weapon("Steel Sword", 6, "Blade", "Steel", 40)