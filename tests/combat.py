#voy a hacer un test de combate simple
import time
from game.entities.player import Player
from game.entities.enemy import Enemy
def test_combat():
    player = Player("Hero", 100, 10)
    enemy = Enemy("Goblin", 50, 5, 15, 25)
    while True:
        #aqui añado un segundo de delay para que se vea mejor el combate
        time.sleep(1)
        if player.health <= 0:
            break
        elif enemy.health <= 0:
            break
        player.attack(enemy)
        enemy.attack(player)