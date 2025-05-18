from world import create_world
from player import Player
from commands import process_command, how_to_play

def main():
    how_to_play()
    start_room = create_world()
    player = Player(start_room)

    while True:
        player.current_room.describe()
        command = input("\n> ")
        if not process_command(player, command):
            break

if __name__ == "__main__":
    main()