class Apparel:
    def __init__(self, name, armor, value):
        self.name = name
        self.armor = armor
        self.value = value

    def __str__(self):
        return f"{self.name} is a piece of armor which provides {self.armor} armor, and is worth {self.value} coins."

nothing = Apparel("Nothing", 0, 0)
rags = Apparel("Rags", 0, 0)
leather_armor = Apparel("Leather Armor", 1, 10)
copper_armor = Apparel("Copper Armor", 2, 20)
bronze_armor = Apparel("Bronze Armor", 3, 30)
iron_armor = Apparel("Iron Armor", 4, 40)
steel_armor = Apparel("Steel Armor", 5, 50)

purchasable_apparel = [leather_armor, copper_armor, bronze_armor, iron_armor, steel_armor]
