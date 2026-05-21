class Apparel:
    def __init__(self, armor, apparel_type, material, value):
        self.armor = armor
        self.apparel_type = apparel_type
        self.material = material
        self.value = value


rags = Apparel(0, "Torso", "Fabric", 0)
leather_armor = Apparel(2, "Torso", "Leather", 10)