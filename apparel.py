class Apparel:
    def __init__(self, name, armor, material, value):
        self.name = name
        self.armor = armor
        self.material = material
        self.value = value

    def __str__(self):
        if self.material == None:
            return f"{self.name} is well, nothing. Just your plain skin, fur or similar."
        else:
            return f"{self.name} is a {self.material} piece of armor which provides {self.armor} armor, and is worth {self.value} coins."

nothing = Apparel("Nothing", 0, None, 0)
rags = Apparel("Rags", 0, "Fabric", 0)
leather_armor = Apparel("Leather Armor", 1, "Leather", 10)
copper_armor = Apparel("Copper Armor", 2, "Copper", 20)
bronze_armor = Apparel("Bronze Armor", 3, "Bronze", 30)
iron_armor = Apparel("Iron Armor", 4, "Iron", 40)
steel_armor = Apparel("Steel Armor", 5, "Steel", 50)
