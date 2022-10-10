class Monster():
    """
        Objectives:
            1. Define the monsters
    """

    def __init__(self, attributes):
        self.power = attributes["power"]
        self.ability = attributes["ability"]
        self.active = False
        self.name = attributes["name"]
        return

    def __repr__(self):
        return f"Power:{self.power}, Ability:'{self.ability}'"

    def __str__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)
