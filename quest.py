"""Functions and classes related to quests."""

class Quest:
    def __init__(self, name, xp_reward, coins_reward, other_reward = None):
        self.name = name
        self.xp_reward = xp_reward
        self.coins_reward = coins_reward
        self.other_reward = other_reward