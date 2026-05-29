"""Functions and classes related to quests."""

class Quest:
    def __init__(self, name: str, level_requirement: int, xp_reward: int, coins_reward: int, other_reward = None):
        self.name = name
        self.level_requirement = level_requirement
        self.xp_reward = xp_reward
        self.coins_reward = coins_reward
        self.other_reward = other_reward