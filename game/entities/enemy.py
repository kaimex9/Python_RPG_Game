class Enemy:
    from game.entities.player import Player
    #Aqui definimos la clase Enemy con sus atributos y métodos
    def __init__(self, name, health, defense, attack_power, experience_value):
        self.name = name
        self.health = health
        self.defense = defense
        self.attack_power = attack_power
        self.experience_value = experience_value

    #Esta es la duncion del monstruo para atacar al jugador
    def attack(self, player: Player):
        
        player.take_damage(self.attack_power)
        print(f"{self.name} attacked {player.name}!")

    #Esta es la función del monstruo para recibir daño del jugador
    def take_damage(self, damage, player: Player):
        final_damage = max(1, damage - self.defense)
        self.health -= final_damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            self.die(player)
        else:
            print(f"{self.name} took {final_damage} damage, remaining health: {self.health}")

    #Esta es la función del monstruo para morir
    def die(self, player: Player):
        print(self.name + " has been defeated!")
        self.drop_exp(player)

    #Esta es la función del monstruo para dar experiencia al jugador
    def drop_exp(self, player: Player):
        player.stats.gain_exp(self.experience_value)
        print(f"{player.name} gained {self.experience_value} experience points!")

