from game.entities.stats import Stats

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = Stats(
            level=1,
            exp=0,
            max_exp=100,
            strenght=5,
            dexterity=5,
            constitution=5,
            intelligence=5,
            charisma=5
        )
