from game.entities.base_character import Character

class Enemy(Character):
    #Aqui definimos la clase Enemy con sus atributos y métodos
    def __init__(self, name, health, damage, defense, experience_value):
        super().__init__(name, health, damage, defense)
        self.damage = damage
        self.experience_value = experience_value
        self.loot_table = []

    #Esta es la duncion del monstruo para atacar al jugador
    def attack(self, player: Character):
        print(f"{self.name} attacked you!")
        player.take_damage(self.damage, self)

    #Esta es la función del monstruo para recibir daño del jugador
    def take_damage(self, damage, player: Character):
        final_damage = max(1, damage - self.defense)
        self.health -= final_damage
        if self.health <= 0:
            self.die(player)
        else:
            print(f"{self.name} took {final_damage} damage, remaining health: {round(self.health)}")

    #Esta es la función del monstruo para morir
    def die(self, player: Character):
        print(self.name + " has been defeated!")
        self.drop_exp(player)

    #Esta es la función del monstruo para dar experiencia al jugador
    def drop_exp(self, player: Character):
        player.stats.gain_exp(player, self.experience_value)

