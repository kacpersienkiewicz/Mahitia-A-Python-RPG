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
copper_sword = Weapon("Copper Sword", 5, "Blade", "Copper", 10)