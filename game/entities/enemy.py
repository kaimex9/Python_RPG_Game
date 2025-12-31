from game.entities.base_character import Character

class Enemy(Character):
    #Aqui definimos la clase Enemy con sus atributos y métodos
    def __init__(self, name, health, defense, attack_power, experience_value):
        super().__init__(name, health, defense)
        self.attack_power = attack_power
        self.experience_value = experience_value

    #Esta es la duncion del monstruo para atacar al jugador
    def attack(self, character: Character):
        print(f"{self.name} attacked you!")
        character.take_damage(self.attack_power, self)
        
    #Esta es la función del monstruo para recibir daño del jugador
    def take_damage(self, damage, character: Character):
        final_damage = max(1, damage - self.defense)
        self.health -= final_damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            self.die(character)
        else:
            print(f"{self.name} took {final_damage} damage, remaining health: {self.health}")

    #Esta es la función del monstruo para morir
    def die(self, character: Character):
        print(self.name + " has been defeated!")
        self.drop_exp(character)

    #Esta es la función del monstruo para dar experiencia al jugador
    def drop_exp(self, player: Character):
        player.stats.gain_exp(self.experience_value)
        print(f"{player.name} gained {self.experience_value} experience points!")

