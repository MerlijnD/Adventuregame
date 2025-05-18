from room import Room
from item import Item, Weapon
from enemy import Enemy

def create_world():
    start_room = Room("Starting room", "You wake up in a large room. There is a door south of you, a corridor to the north, a room to the west and a locked door to the east.")
    outside = Room("Outside", "You open the door and escape the house. Congratulations on escaping!")
    second_room = Room("Study room", "You enter a room that looks like a workspace. It has a large desk with some papers and a key on top.")
    third_room = Room("Kitchen", "You enter the kitchen. You see some pots and pans and one big knife.")
    fourth_room = Room("Hallway", "You see a room to the north but hear movement coming from it. Make sure to be prepared before you continue.")
    fifth_room = Room("Goblin room", "You see a goblin and it attacks you! If you defeat the goblin you see a key on his belt.")
        
    kitchen_key = Item("small key", "A small key with a pan on the keychain.")
    house_key = Item("large key", "A key that is shaped like a house.")

    knife = Weapon("knife", "A large but old knife", 20)

    goblin = Enemy("Goblin", 40, "knife", 20, drop_item=house_key)

    start_room.exits["north"] = fourth_room
    start_room.exits["west"] = second_room
    start_room.locked_exits["east"] = {"key": "small key", "room": third_room}
    start_room.locked_exits["south"] = {"key": "large key", "room": outside}

    second_room.exits["east"] = start_room

    third_room.exits["west"] = start_room

    fourth_room.exits["north"] = fifth_room
    fourth_room.exits["south"] = start_room

    fifth_room.exits["south"] = fourth_room

    second_room.items.append(kitchen_key)
    third_room.items.append(knife)

    fifth_room.enemies.append(goblin)

    return start_room