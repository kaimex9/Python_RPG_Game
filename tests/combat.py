#voy a hacer un test de combate simple
import time
from game.entities.player import Player
from game.entities.enemy import Enemy
def test_combat():
    player = Player("Hero", 100, 10)
    enemy = Enemy("Goblin", 30, 1, 50, 25)
    while True:
        time.sleep(1)
        player.attack(enemy)
        if enemy.health <= 0:
            break
        enemy.attack(player)
        if player.health <= 0:
            break
        