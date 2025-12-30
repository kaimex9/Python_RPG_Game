# game/engine/game_loop.py

def allocate_stat_point(stats):
    print("\nYou gained a level! You have 1 stat point to allocate.")
    print("Choose a stat to increase:")
    print("1. Strength:", stats.strenght)
    print("2. Dexterity:", stats.dexterity)
    print("3. Constitution:", stats.constitution)
    print("4. Intelligence:", stats.intelligence)
    print("5. Charisma:", stats.charisma)

    choice = input("Enter the number: ")

    mapping = {
        "1": "strenght",
        "2": "dexterity",
        "3": "constitution",
        "4": "intelligence",
        "5": "charisma"
    }

    stat_name = mapping.get(choice)

    if stat_name:
        stats.increase_stat(stat_name)
        print( "Your " + stat_name + " has been increased!" )
    else:
        print("Invalid choice.")