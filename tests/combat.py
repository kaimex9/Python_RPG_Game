#voy a hacer un test de combate simple

from game.entities.player import Player
from game.entities.enemy import Enemy
def test_combat():
    player = Player("Hero", 100, 10)
    enemy = Enemy("Goblin", 50, 5, 15, 25)
    player.attack(enemy)
    enemy.attack(player)