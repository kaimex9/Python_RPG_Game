from tests.combat import test_combat
from game.entities.player import Player
from game.items.weapon import Weapon

if __name__ == "__main__":
    #test_combat()
    player = Player("Hero", 100, 1, 5)
    weapon = Weapon(
        name="Sword of Testing",
        description="A sword used for testing combat.",
        weight=5,
        value=100,
        rarity="Common",
        slot="Weapon",
        base_damage=10,
        scaling={"strenght": "B"},
        requirements={"level": 1} #Aparte de nivel quiero que necesites una cantidad de stats
    )
    player.inventory.append(weapon)
    player.inventory.append(weapon)
    player.inventory.append(weapon)
    player.inventory.append(weapon)
    player.inventory.append(weapon)
    player.inventory.append(weapon)
    print("mi daño es:", player.calculate_damage())
    while True:
        print("---------------------------------------------------")
        print("Tu arma equipada es:", player.equipment[5].name if player.equipment[5] else "Ninguna")
        print("[1]Combat")
        print("[2]Show Inventory")
        print("[3]Show Equipment")
        print("[4]Equip something")
        choice = input("Choose an option: ")
        if choice == "1":
            test_combat(player)
        elif choice == "2":
            player.show_inventory()
        elif choice == "3":
            player.show_equipment()
        elif choice == "4":
            item_name = input("Enter the name of the item to equip: ")
            item = player.find_item_by_name(item_name)
            if item:
                item.equip(player)
            else:
                print("Item not found in inventory.")
        else:
            print("bye.")
            break
    
                    