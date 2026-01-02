#voy a hacer un test de combate simple
import time
from game.entities.player import Player
from game.entities.enemy import Enemy
from game.items.weapon import Weapon
def test_combat(player=Player):
    enemy = Enemy("Goblin", 30, 1, 5, 25)
    
    while True:
        time.sleep(1)
        player.attack(enemy)
        if enemy.health <= 0:
            break
        enemy.attack(player)
        if player.health <= 0:
            break
        