class Stats:

    def __init__(self, level, exp, max_exp, strenght, dexterity, constitution, intelligence, charisma):
        self.level = level
        self.exp = exp
        self.max_exp = max_exp

        self.strenght = strenght
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.charisma = charisma

        self.stat_points = 0

    def gain_exp(self, amount):
        self.exp += amount

        while self.exp >= self.max_exp:
            self.exp -= self.max_exp
            self.level_up()
            self.max_exp = int(self.max_exp * 1.5)

    def level_up(self):
        self.level += 1
        self.stat_points += 1

    def increase_stat(self, stat_name):
        if self.stat_points <= 0:
            return False

        if stat_name == "strenght":
            self.strenght += 1
        elif stat_name == "dexterity":
            self.dexterity += 1
        elif stat_name == "constitution":
            self.constitution += 1
        elif stat_name == "intelligence":
            self.intelligence += 1
        elif stat_name == "charisma":
            self.charisma += 1
        else:
            return False

        self.stat_points -= 1
        return True