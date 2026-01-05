class Item:
    def __init__(self, name, description, weight, value, rarity, slot):
        self.name = name
        self.description = description
        self.weight = weight
        self.value = value
        self.rarity = rarity
        self.slot = slot

    def inspect(self):
        # Aqui quiero devolver todos los atributos del item en fila de arriba a abajo
        return (f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Weight: {self.weight}\n"
                f"Value: {self.value}\n"
                f"Rarity: {self.rarity}\n"
                f"Slot: {self.slot}")
    
    #Aqui faltan muchos comprobantes en cada caso pero bueno
    def equip(self, player):
        if(player.add_weight(self.weight)):
            match self.slot:
                case "Head":
                    player.equipment[0] = self
                    print(f"You have equipped {self.name} on your Head.")
                case "Chest":
                    player.equipment[1] = self
                    print(f"You have equipped {self.name} on your Chest.")
                case "Hands":
                    player.equipment[2] = self
                    print(f"You have equipped {self.name} on your Hands.")
                case "Legs":
                    player.equipment[3] = self
                    print(f"You have equipped {self.name} on your Legs.")
                case "Feet":
                    player.equipment[4] = self
                    print(f"You have equipped {self.name} on your Feet.")
                case "Weapon":
                    player.equipment[5] = self
                    print(f"You have equipped {self.name} as your Weapon.")
                case _:
                    print("You cannot equip this item.")