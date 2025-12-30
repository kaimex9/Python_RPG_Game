from game.entities.stats import Stats
from game.entities.enemy import Enemy

class Player:

    def __init__(self, name, health, defense):
        self.name = name
        self.health = health
        self.defense = defense
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
    def attack(self, enemy: Enemy):
        enemy.take_damage(self.stats.strenght, self)
        print(f"{self.name} attacked you!.")

    #Esta es la función del jugador para recibir daño del enemigo
    def take_damage(self, damage, enemy: Enemy):
        final_damage = max(1, damage - self.defense)
        self.health -= final_damage
        if self.health <= 0:
            self.die(enemy)
        else:
            print(f"you took {final_damage} damage, remaining health: {self.health}")

    #Esta es la función del jugador para morir
    def die(self, enemy: Enemy):
        print("Game Over! The player has been defeated.")