import random
import time



advantages = {
    "shadow": "light",
    "light": "water",
    "water": "fire",
    "fire": "shadow"
}


class Character:

    def __init__(self, name, class_type):

        self.name = name
        self.class_type = class_type
        self.hp = 200
        self.adaptation = 10

    def attack(self, enemy):

        damage = random.randint(1, 100)

        if advantages[enemy.class_type] == self.class_type:

            print("\n" + self.class_type,
                  "has an advantage over",
                  enemy.class_type, end="... ")

            original_damage = damage
            damage -= enemy.adaptation

            print(f"{enemy.class_type} adapted to the attack, {enemy.adaptation} damage reduced! (From {original_damage} to {damage})")

            if damage < 0:
                damage = 0

            print("ATTACK ADAPTED")

            enemy.adaptation += 5

        enemy.hp -= damage

        print("\n" + self.name,
              "dealt",
              damage,
              "damage to",
              enemy.name)

        return damage


def choose_class(player_name):

    while True:

        print("--------------CLASSES--------------")
        print("Shadow", end="  ")
        print("Light", end="  ")
        print("Fire", end="  ")
        print("Water")

        choice = input(player_name +
                       " choose your class: ")

        if choice.lower() in advantages:
            return choice

        else:
            print("Invalid class! Try again.")


while True:

    while True:

        start = input(
            "\nPress S to start game or Q to quit: ")

        if start.lower() == "s":
            break

        elif start.lower() == "q":
            quit()

        else:
            print("Invalid input!")

    print("--------------loading game--------------")
    print(" please wait", end="..." "\n")
    time.sleep(2)
    print("--------------------------------------------WELCOME TO THE BATTLE OF GODS--------------------------------------------------")
    print("\n" + "="*50)
    print("GAME RULES:")
    print("- Two players battle using elemental classes: Shadow, Light, Fire, Water.")
    print("- Some classes have advantages over others, but you'll discover them in battle!")
    print("- Each player starts with 200 HP. Attack to deal damage.")
    print("- Enemies may adapt to your attacks, reducing damage over time.")
    print("- First to reduce the opponent's HP to 0 or below wins!")
    print("- Press Enter to attack each turn. No defending—strategy is key!")
    print("="*50)
    time.sleep(2)
    name1 = input("\nPlayer 1 enter your name: ")


    print(name1, "HAS ENTERED THE BATTLEFIELD OF GODS!")

    print("loading...")
    time.sleep(2)
    print("\n PLEASE SELECT YOUR CLASS")
    class1 = choose_class(name1)
    time.sleep(1)

    name2 = input("\nPlayer 2 enter your name: ")
    print(name2, "HAS ENTERED THE BATTLEFIELD OF GODS!")
    print("loading...")
    time.sleep(2)
    print("PLEASE SELECT YOUR CLASS")
    class2 = choose_class(name2)
    time.sleep(1)

    print("")
    print("")
    time.sleep(1)

    print("-----------LET THE BATTLE BEGIN-----------")
    print("")
    print("The gods clash in an epic elemental showdown!")
    print("loading...")
    time.sleep(2)

    player1 = Character(name1, class1)
    player2 = Character(name2, class2)

    current_player = random.choice(
        [player1, player2])

    if current_player == player1:
        other_player = player2
    else:
        other_player = player1

    print("\n" + current_player.name,
          "will attack first!")

    turn_count = 0
    total_damage_p1 = 0
    total_damage_p2 = 0

    while True:

        input("\n" + current_player.name +
              " press Enter to attack...")
        time.sleep(0.5)

        damage_dealt = current_player.attack(other_player)
        time.sleep(1.5)

        if current_player == player1:
            total_damage_p1 += damage_dealt
        else:
            total_damage_p2 += damage_dealt

        turn_count += 1

        print("\n////////////////////Remaining HP////////////////////")
        print(player1.name,
              "(" + player1.class_type + ")",
              "- HP:", player1.hp, "| Adaptation:", player1.adaptation)

        print(player2.name,
              "(" + player2.class_type + ")",
              "- HP:", player2.hp, "| Adaptation:", player2.adaptation)

        if other_player.hp <= 0:

            print()

            if other_player.hp < -25:
                print("CRITICAL HIT")

            print(other_player.name, "DOWN")
            print(current_player.name, "WINS")
            time.sleep(2)

            print("\n" + "="*50)
            print("MATCH SUMMARY:")
            print(f"Total Turns: {turn_count}")
            print(f"{name1} ({class1}) - Total Damage Dealt: {total_damage_p1} | Final HP: {player1.hp} | Final Adaptation: {player1.adaptation}")
            print(f"{name2} ({class2}) - Total Damage Dealt: {total_damage_p2} | Final HP: {player2.hp} | Final Adaptation: {player2.adaptation}")
            print(f"Winner: {current_player.name} ({current_player.class_type})")
            print("="*50)
            time.sleep(1)

            break

        current_player, other_player = (
            other_player,
            current_player
        )

    while True:

        rematch = input(
            "\nPress T to rematch or Q to quit: ")

        if rematch.lower() == "t":
            break

        elif rematch.lower() == "q":
            quit()

        else:
            print("Invalid input!")