from game.items.item import Item

class Armor(Item):
    def __init__(self, name, description, weight, value, rarity, slot, defense):
        super().__init__(name, description, weight, value, rarity, slot)
        self.defense = defense
        self.slot = slot

    def inspect(self):
        base_inspect = super().inspect()
        return f"{base_inspect}\nDefense: {self.defense}\nSlot: {self.slot}"