class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {} # Dictionary of exits out of the room
        self.locked_exits = {} # Dictionary of locked exits
        self.items = [] # List of items in the rooms
        self.enemies = [] # List of enemies in the room

    def describe(self):
        print(f"\n{self.name}")
        print(self.description)

        if self.items:
            item_names = [item.name for item in self.items]
            print("You see: " + ", ".join(item_names))

        available_exits = list(self.exits.keys()) + list(self.locked_exits.keys())
        if available_exits:
            print("Exits: " + ", ".join(available_exits))

        if self.enemies:
            enemy_names = [enemy.name for enemy in self.enemies]
            print("Enemies here: " + ", ".join(enemy_names))

    def unlock(self, direction, item_name):
        if direction in self.locked_exits and self.locked_exits[direction]["key"] == item_name:
            self.exits[direction] = self.locked_exits[direction]["room"] 
            del self.locked_exits[direction] # Remove from locked exits
            print(f"You unlocked the door to the {direction}!")
            return True
        print("That item doesn't work here.")
        return False