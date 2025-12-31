class Character:
    def __init__(self, name, health, defense):
        self.name = name
        self.health = health
        self.defense = defense

    def take_damage(self, damage):
        final_damage = max(1, damage - self.defense)
        self.health -= final_damage
        return final_damage
