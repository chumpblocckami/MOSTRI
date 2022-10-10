import os

from dotenv import load_dotenv

load_dotenv()

N_MONSTER = int(os.getenv('N_MONSTER'))


class Cage():
    """
        Objectives:
            1. Holds the monsters
            2. Apply activation policies (monsters in hand)

    """

    def __init__(self, bestiare):
        self.bestiare = bestiare
        self.monsters = self.tame_monsters(n_monsters=N_MONSTER)
        return

    def tame_monsters(self, n_monsters):
        monsters = [self.bestiare.simple_capture() for _ in range(0, n_monsters)]
        activated_monsters = self.simple_activation_policy(monsters)
        return activated_monsters

    def simple_activation_policy(self, monsters):
        for n in range(0, len(monsters)):
            if n >= 5:
                monsters[n].active = True
        return monsters

    def very_complex_activation_policy(self):
        """
            Capturing a creature might be difficult based on aggressivity, diet, emotions...........
        """
        return

    def __getitem__(self, i):
        return self.monsters[i]

    def __len__(self):
        return len(self.monsters)

    def __repr__(self):
        return "\n".join([str(monster) for monster in self.monsters])
