import json
import random

from monster import Monster

import copy

class Bestiare():
    """
        Objectives:
            1. Creates the monsters.
            2. Define capture policy
    """

    def __init__(self):
        self.population = self.open_bestiare()
        return

    def open_bestiare(self):
        bestiare = []
        with open("monster_data.json", "r+") as file:
            monsters_data = json.loads(file.read())
        file.close()
        for monster in monsters_data:
            for _ in range(0, monster["rarity"]):
                bestiare.append(Monster(attributes=monster))
        return bestiare

    def simple_capture(self):
        beast_idx = random.randint(0, len(self.population))
        beast_idx = beast_idx-1 if beast_idx != 0 else 0
        if beast_idx == -1:
            return None
        creature_picked = self.population[beast_idx]
        del self.population[beast_idx]
        return creature_picked

    def very_complex_capture(self):
        """
            Capturing a creature might be difficult based on rarity, terrain, weather conditions......
        """
        return

    def __getitem__(self, i):
        return self.population[i]

    def __len__(self):
        return len(self.population)

    def __repr__(self):
        return "\n".join([str(monster) for monster in self.population])