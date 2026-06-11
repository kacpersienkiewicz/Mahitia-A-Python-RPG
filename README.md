# Mahitia A Python RPG
You start in a small hunting and farming town of Scrimshaw, trying to make your way in the world. The max level is 10 and there is an intended final quest, but you can still play afterwards.

## Technical
* I created a class for equipment (weapon, apparel), quests, and characters (including a subclass for players).
  * This also includes several instances for each object, including five tiers of purchasable weapons and armor.
* Four quests: 2 intro level, 1 medium level and one hard quest.
* Three monster lists: weak, moderate and hard. This also includes the same tiers for each attribute to create new enemies fairly easily.
* Created a function to simplify the code for shopping.
  * Basically, it checks what instance an item is (weapon or apparel, for example) and then formats a table based off of that.
