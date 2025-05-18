class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {} # Dictionary of exits out of the room
        self.items = [] # List of items in the rooms

    def describe(self):
        print(f"\n{self.name}")
        print(self.description)
        if self.items:
            print("You see: " + ", ".join(self.items))
        if self.exits:
            print("Exits: " + ", ".join(self.exits.keys()))


class Item:
    pass

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"You move {direction}.")
        else:
            print("You can't go that way!")

def create_world():
    start_room = Room("Starting room", "You wake up in a large room. There is a door behind you and a corridor to the north.")
    second_room = Room("Hallway", "You see a room to the north but hear growling coming from it.")

    start_room.exits["north"] = second_room
    second_room.exits["south"] = start_room

    start_room.items.append("knife")

    return start_room

def main():
    start_room = create_world()
    player = Player(start_room)

    while True:
        player.current_room.describe()
        command = input("\n> ").strip().lower()

        if command in ["quit", "exit"]:
            print("Thanks for playing!")
            break
        elif command.startswith("go "):
            direction = command.split(" ", 1)[1]
            player.move(direction)
        elif command.startswith("take "):
            item = command.split(" ", 1)[1]
            if item in player.current_room.items:
                player.current_room.items.remove(item)
                player.inventory.append(item)
                print(f"You picked up the {item}.")
            else:
                print("That item is not here.")
        elif command == "inventory":
            print("Inventory: ", ", ".join(player.inventory) if player.inventory else print("Your inventory is empty."))
        else:
            print("Unknown command. Try 'go [direction]', 'take [item]' or 'inventory'.")

if __name__ == "__main__":
    main()