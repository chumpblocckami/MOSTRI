import os

from dotenv import load_dotenv

from cage import Cage
from graveyard import Graveyard

load_dotenv()

N_COMMANDEERS = os.getenv('N_COMMANDEERS')
LIFE = os.getenv('LIFE')


class Tamer():
    """
        Objectives:
            1. Define player monsters
            2. Define number of commandeer
            3. Define graveyard
    """

    def __init__(self, bestiare):
        self.cage = Cage(bestiare)
        self.graveyard = Graveyard()
        self.n_commandeer = N_COMMANDEERS
        self.lifes = LIFE
        return
