"""Functions and classes related to quests."""
import character
import combat 

class Quest:
    def __init__(self, name: str, level_requirement: int, completed: bool, quest_function: function,  xp_reward: int, coins_reward: int, other_reward = None):
        self.name = name
        self.level_requirement = level_requirement
        self.completed = completed
        self.quest_function = quest_function
        self.xp_reward = xp_reward
        self.coins_reward = coins_reward
        self.other_reward = other_reward

def quest_function_goblin_encampment(player, quest: Quest):
    """The Player is tasked with defeating a goblin warrior at a local goblin encampment that is troubling Scrimshaw."""
    print("You wander into the nearby woods searching for the goblin encampment when you were suddenly attacked by a goblin.")
    combat.monster_encounter(player, character.goblin)

    print("The goblin had a note detailing orders on her. The handwriting is awful, but you figure you need to follow the river and so go that way.")
    print("You see the encampment but are attacked by two goblins.")
    combat.monster_encounter(player, character.goblin)
    combat.monster_encounter(player, character.goblin)

    print("Those two goblins were the warrior's personal guard. They were branded with a goblin's hand upon their face. A shriek echoes in the encampment as a well armed goblin, the warrior, challenges you.")
    combat.monster_encounter(player, character.goblin_warrior)

    print("The warrior is dead, and your job is done, but if you want you can loot the rest of encampment, killing the rest of the goblins and gaining some gold.")
    while True:
        choice = input(f"Would you like to fight some more goblins and get some more loot? [y/n]?\n")
        if choice == 'y':
            print("The encampment is dead silent, so you keep your guard up. Wandering through the storage house, you find 25 coins and a goblin.")
            player.coins += 25
            combat.monster_encounter(player, character.goblin)
            print("The goblin was no match for you. You now move onto looking through the barracks. The barracks have two quivering goblins who reluctantly start fighting.")
            combat.monster_encounter(player, character.goblin)
            combat.monster_encounter(player, character.goblin)
            print("You don't find much of value in the barracks. The only building is the assumed office for the warrior. Inside, two wolves wake up as you enter.")
            combat.monster_encounter(player, character.wolf)
            combat.monster_encounter(player, character.wolf)
            print("You find 50 gold worth of trinkets throughout the office.")
            player.coins += 50
            print("You explored each building at the encampment and are ready to head out.")
            break
        elif choice == 'n':
            break
        else:
            print("Only 'y' or 'n' are valid inputs. Please enter one of those.")
            continue

    print("You head back to the inn to get your reward.")
    player.xp += quest.xp_reward
    player.coins += quest.coins_reward
    quest.completed = True

def quest_function_forest_cleanup(player, quest: Quest):
    """The local forest has an overpopulation of wolves, which the player is tasked with culling."""
    print("Even from far away, the forest is obviously overrun with wolves. You can't see too many deer ")

    print("You head back to the inn to get your reward.")
    player.xp += quest.xp_reward
    player.coins += quest.coins_reward
    quest.completed = True

def quest_function_bandit_lord_showdown(player, quest: Quest):
    """A bandit lord has challenged the player, and the player takes the challenge."""
    print("You head back to the inn to get your reward.")
    player.xp += quest.xp_reward
    player.coins += quest.coins_reward
    quest.completed = True

def quest_function_dark_knights_fortress(player, quest: Quest):
    """The source of local troubles is pinned on a Dark Knight's Fortress. The Player is tasked with defeating the Dark Knights."""
    print("You head back to the inn to get your reward.")
    player.xp += quest.xp_reward
    player.coins += quest.coins_reward
    quest.completed = True

quest_goblin_encampment = Quest("Goblin Encampment", 0, False, quest_function_goblin_encampment, 100, 50)
quest_forest_cleanup = Quest("Forest Cleanup", 0, False, quest_function_forest_cleanup, 100, 50)
quest_bandit_lord_showdown = Quest("Bandit Lord Showdown", 5, False, quest_function_bandit_lord_showdown, 250, 100)
quest_dark_knights_fortress = Quest("Dark Knight's Fortress", 10, False, quest_function_dark_knights_fortress, 350, 150)