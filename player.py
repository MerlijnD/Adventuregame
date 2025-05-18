from item import Weapon

class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []
        self.health = 100

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"You move {direction}.")
        elif direction in self.current_room.locked_exits:
            print("This door is locked.")
        else:
            print("You can't go that way!")
    
    def take_item(self, item_name):
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                self.current_room.items.remove(item)
                self.inventory.append(item)
                print(f"You picked up the {item}.")
                return
        print("That item is not here.")

    def show_inventory(self):
        if self.inventory:
            print("Inventory: ")
            for item in self.inventory:
                print(f"- {item.name}: {item.description}")
        else:
            print("Your inventory is empty.")

    def unlock_door(self, direction, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if self.current_room.unlock(direction, item.name):
                    self.inventory.remove(item) # Remove key after use
                return
        print(f"You don't have {item_name}.")

    def attack(self, enemy_name, weapon_name):
        enemy = next((e for e in self.current_room.enemies if e.name.lower() == enemy_name.lower()), None)
        if not enemy_name:
            print("This enemy is not here.")
            return
        
        weapon = next((w for w in self.inventory if isinstance(w, Weapon) and w.name.lower() == weapon_name.lower()), None)
        if not weapon:
            print("You do not have that weapon.")
            return
        
        print(f"You attack {enemy.name} with {weapon.name}!")
        if enemy.take_damage(weapon.damage):
            self.current_room.enemies.remove(enemy) # Remove enemy if defeated
            if enemy.drop_item:
                self.current_room.items.append(enemy.drop_item)
                print(f"The {enemy.name} dropped a {enemy.drop_item.name}!")
        else:
            self.health -= enemy.damage
            if self.health <= 0:
                print(f"The enemy does {enemy.damage} damage to you and is too strong for you. The enemy kills you.")
                exit()
            else:
                print(f"The enemy hits back! It did {enemy.damage} damage to you. Your current health is {self.health}.")