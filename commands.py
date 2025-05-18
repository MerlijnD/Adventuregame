def how_to_play():
    print('''HOW TO PLAY: \n
          This is a text based game and everything happens in the terminal.\n
          You can always quit the game by typing: "quit" or "exit"\n
          To move around type: "go [direction]"\n
          To pick up an item type: "take [item]"\n
          To unlock a locked door type: "unlock [direction] with [item]"\n
          To see what is in your inventory type: "inventory"\n
          To attack an enemy type: "attack [enemy] with [item]"\n
          To read the commands again type: "help" or "how to play"\n
          Enjoy the game!\n''')

def process_command(player, command):
    command = command.strip().lower()

    if command in ["quit", "exit"]:
        print("Thanks for playing!")
        return False
    elif command.startswith("go "):
        direction = command.split(" ", 1)[1]
        player.move(direction)
    elif command.startswith("take "):
        item_name = command.split(" ", 1)[1]
        player.take_item(item_name)
    elif command.startswith("unlock "):
        parts = command.split(" with ", 1)
        if len(parts) == 2:
            direction = parts[0].replace("unlock ", "", 1)
            item_name = parts[1]
            player.unlock_door(direction, item_name)
        else:
            print("Use: unlock [direction] with [item]")
    elif command == "inventory":
        player.show_inventory()
    elif command.startswith("attack "):
        parts = command.split(" with ", 1) # Expect attack [enemy] with [weapon]
        if len(parts) == 2:
            enemy_name = parts[0].replace("attack ", "", 1)
            weapon_name = parts[1]
            player.attack(enemy_name, weapon_name)
        else:
            print("Use: attack [enemy] with [weapon]")
    elif command in ["help", "how to play"]:
        how_to_play()
    else:
        print("Unknown command. Try 'go [direction]', 'take [item]' or 'inventory'.")

    return True