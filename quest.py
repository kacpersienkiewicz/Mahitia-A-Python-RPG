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
    """The Player is tasked with defeating a goblin captain at a local goblin encampment that is troubling Scrimshaw."""
    print("You wander into the nearby woods searching for the goblin encampment when you were suddenly attacked by a goblin.")
    combat.monster_encounter(player, character.goblin)

    print("The goblin had a note detailing orders on her. The handwriting is awful, but you figure you need to follow the river and so go that way.")
    print("You see the encampment but are attacked by two goblins.")
    combat.monster_encounter(player, character.goblin_warrior)
    combat.monster_encounter(player, character.goblin_warrior)

    print("Those two goblins were the captain's personal guard. They were branded with a goblin's hand upon their face. A shriek echoes in the encampment as a well armed goblin, the captain, challenges you.")
    combat.monster_encounter(player, character.goblin_captain)

    print("The captain is dead, and your job is done, but if you want you can loot the rest of encampment, killing the rest of the goblins and gaining some gold.")
    while True:
        choice = input(f"Would you like to fight some more goblins and get some more loot? [y/n]?\n")
        if choice == 'y':
            print("The encampment is dead silent, so you keep your guard up. Wandering through the storage house, you find 25 coins and a goblin.")
            player.coins += 25
            combat.monster_encounter(player, character.goblin)
            print("The goblin was no match for you. You now move onto looking through the barracks. The barracks have two quivering goblins who reluctantly start fighting.")
            combat.monster_encounter(player, character.goblin)
            combat.monster_encounter(player, character.goblin)
            print("You don't find much of value in the barracks. The only building is the assumed office for the captain. Inside, two wolves wake up as you enter.")
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
    print("Even from far away, the forest is obviously overrun with wolves. You can't see too many deer around. Two wolves spot you and engage.")
    combat.monster_encounter(player, character.wolf)
    combat.monster_encounter(player, character.wolf)

    print("After the fight, you can hear howling start to pick up, including a deep howl that you feel in your chest. At this point, three wolves circle you and attack.")
    combat.monster_encounter(player, character.wolf)
    combat.monster_encounter(player, character.wolf)
    combat.monster_encounter(player, character.wolf)

    print("The howling starts to subside but the deeper howling grows and grows until you see a massive wolf, with deep red eyes. It lunged at your immediately.")
    combat.monster_encounter(player, character.wolf_dire)

    print("You defeated the dire wolf, and all howling subsides. Seems like the town is saved.")

    print("You head back to the inn to get your reward.")
    player.xp += quest.xp_reward
    player.coins += quest.coins_reward
    quest.completed = True

def quest_function_bandit_lord_showdown(player, quest: Quest):
    """A bandit lord has challenged the player, and the player takes the challenge."""
    print("Bandits don't typically openly challenge people. They skulk in the shadows near the road and ambush unsuspecting travelers, but this one is different. They wait at the town's center for you.")
    print("As expected, the bandit lord is found at the center of town, but they're with an entourage.\nThe Bandit Lord screams: 'Prove your worth before you can face me worm!'\nYou are attacked by three bandits.")

    combat.monster_encounter(player, character.bandit)
    combat.monster_encounter(player, character.bandit)
    combat.monster_encounter(player, character.bandit)

    print("You were easily able to take care of the bandits, and the bandit lord is strangely satisfied with your performance.\n'Excellent. Now defeat my personal guard'\nYou are attacked by two better armed bandits.")
    combat.monster_encounter(player, character.bandit_highwayman)
    combat.monster_encounter(player, character.bandit_highwayman)

    print("The Bandit Lord seems incredibly excited now and exclaims: 'Finally, a challenge' and lunges at you.")
    combat.monster_encounter(player, character.bandit_lord)

    print("With the Bandit Lord dead and looted, you can leave this strange chapter of your life behind.")

    print("You head back to the inn to get your reward.")
    player.xp += quest.xp_reward
    player.coins += quest.coins_reward
    quest.completed = True

def quest_function_dark_knights_fortress(player, quest: Quest):
    """The source of local troubles is pinned on a Dark Knight's Fortress. The Player is tasked with defeating the Dark Knights."""
    print("After speaking with Fred the Farmer, you are able to figure out where the fortress is. You see two entrances: the large front double door, and a side entrance.")
    while True:
        choice = input("Which path do you want to take?\n\t1. Front Door \n\t2. Side Entrance\n")
        if choice == '1':
            print("Usurprisingly, the front path is guarded, by a few dark squires.")
            combat.monster_encounter(player, character.dark_squire)
            combat.monster_encounter(player, character.dark_squire)

            print("You find a key which is able to open the large double doors, leading to a great hall and several more squires.")
            combat.monster_encounter(player, character.dark_squire)
            combat.monster_encounter(player, character.dark_squire)
            combat.monster_encounter(player, character.dark_squire)

            print("The screams of the dying squires draws two dark knights into the hall to fight you.")
            combat.monster_encounter(player, character.dark_knight)
            combat.monster_encounter(player, character.dark_knight)

            break

        elif choice == '2':
            print("For some reason, the side entrance is unlocked and leads into a food preparation area with a single dark squire in it.")
            combat.monster_encounter(player, character.dark_squire)

            print("You're able to sneak around fairly easily leading to a great hall which has a few squires and a dark knight within. They unfortunately spot you and egage you.")
            combat.monster_encounter(player, character.dark_squire)
            combat.monster_encounter(player, character.dark_squire)
            combat.monster_encounter(player, character.dark_knight)

            print("The dark knight is dead but another one appears with an entourage of two squires.")
            combat.monster_encounter(player, character.dark_knight)
            combat.monster_encounter(player, character.dark_squire)
            combat.monster_encounter(player, character.dark_squire)

            break

        else:
            print("Only '1' or '2' are valid inputs. Please enter one of those.")
            continue
        
    print("With two knights and several squires dead, the dark knight's fortress is effectively debarbed.")
    print("You head back to the inn to get your reward.")
    player.xp += quest.xp_reward
    player.coins += quest.coins_reward
    quest.completed = True

quest_goblin_encampment = Quest("Goblin Encampment", 0, False, quest_function_goblin_encampment, 100, 50)
quest_forest_cleanup = Quest("Forest Cleanup", 0, False, quest_function_forest_cleanup, 100, 50)
quest_bandit_lord_showdown = Quest("Bandit Lord Showdown", 5, False, quest_function_bandit_lord_showdown, 250, 100)
quest_dark_knights_fortress = Quest("Dark Knight's Fortress", 10, False, quest_function_dark_knights_fortress, 350, 150)