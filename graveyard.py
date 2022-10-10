class Graveyard():
    """
        Objectives:
            1. Holds tombs
    """

    def __init__(self):
        self.tombs = []

    def __getitem__(self, i):
        return self.tombs[i]

    def __len__(self):
        return len(self.tombs)

    def __repr__(self):
        return "-".join([f"Tomb:{tomb}'" for tomb in self.tombs])
