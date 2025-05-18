class Enemy:
    def __init__(self, name, health, weakness, damage, drop_item = None):
        self.name = name
        self.health = health
        self.weakness = weakness
        self.damage = damage
        self.drop_item = drop_item

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"The {self.name} has been defeated!")
            return True # Enemy is killed
        else:
            print(f"{self.name} has {self.health} remaining.")
            return False # Enemy still alive
        
    def __str__(self):
        return self.name