from game.items.item import Item
from game.utils.scaling_values import SCALING_VALUES

class Weapon(Item):
    def __init__(self, name, description, weight, value, rarity, slot, base_damage, scaling, requirements):
        super().__init__(name, description, weight, value, rarity, slot)
        self.base_damage = base_damage
        self.scaling = scaling 
        self.requirements = requirements
    
    #Funcion para inspeccionar las armas
    def inspect(self):
        base_inspect = super().inspect()
        return (f"{base_inspect}\n"
                f"Base Damage: {self.base_damage}\n"
                f"Scaling: {self.scaling}\n"
                f"Requirements: {self.requirements}")
    
    
    #Esto es para calcular el daño total del arma basado en las estadisticas del jugador, aun asi ni idea de como funciona xd
    def calculate_damage(self, player_stats):
        total_damage = self.base_damage
        for stat, grade in self.scaling.items():
            scaling_value = SCALING_VALUES[grade]
            stat_value = getattr(player_stats, stat)
            total_damage += stat_value * scaling_value
        return total_damage
    
    def can_equip(self, player_stats):
        pass