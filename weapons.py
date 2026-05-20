class Weapon:
    def __init__(self, damage, weapon_type, material, value):
        self.damage = damage
        self.weapon_type = weapon_type
        self.material = material
        self.value = value

    def attack(self, target) -> None:
        target.health -= (self.damage - target.armor)

class rangedWeapon(Weapon):
    def __init__(self, damage, weapon_type, material, value, range):
        super().__init__(damage, weapon_type, material, value)
        self.range = range