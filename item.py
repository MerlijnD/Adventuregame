class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name
    
    def describe(self):
        print(f"{self.name}: {self.description}")

class Weapon:
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def __str__(self):
        return self.name
    
    def describe(self):
        print(f"{self.name}: {self.description}. It does {self.damage} damage")