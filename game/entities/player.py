from game.entities.stats import Stats
from game.entities.base_character import Character
from game.items.weapon import Weapon

class Player(Character):

    def __init__(self, name, health, damage, defense):
        super().__init__(name, health, damage, defense)
        self.inventory = []
        self.equipment = [None] * 6  # Head, Chest, Hands, Legs, Feet, Weapon
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
    #Esta es la función del jugador para atacar al enemigo
    def attack(self, enemy: Character):
        total_damage = self.calculate_damage()
        print("You attacked.")
        enemy.take_damage(total_damage, self)

    def calculate_damage(self):
        base_damage = self.damage
        if self.equipment[5] is not None:  # Assuming weapon is at index 5
            base_damage = base_damage + self.equipment[5].calculate_damage(self.stats)
        return base_damage

    #Esta es la función del jugador para recibir daño del enemigo
    def take_damage(self, damage, enemy: Character):
        final_damage = max(1, damage - self.defense)
        self.health -= final_damage
        if self.health <= 0:
            self.die(enemy)
        else:
            print(f"you took {final_damage} damage, remaining health: {self.health}")

    
    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
            return

        print("Inventory:")
        # 1. Crear un diccionario vacío para contar
        counts = {}

        # 2. Recorrer cada item del inventario
        for item in self.inventory:
            name = item.name
            # 3. Si el nombre ya existe en el diccionario, sumamos 1
            if name in counts:
                counts[name] += 1
            else:
                # 4. Si no existe, lo creamos con valor 1
                counts[name] = 1
        # 5. Mostrar el resultado
        for name, amount in counts.items():
            print(f"- {name} x{amount}")


    def show_equipment(self):
        pass

    def find_item_by_name(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return item
        return None

    #Esta es la función del jugador para morir
    def die(self):
        print("Game Over! The player has been defeated.")
        # Aqui queda pendiente intentar finalizar la partida despues de morir