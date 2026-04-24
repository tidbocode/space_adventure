from .rooms import Room, setup_rooms
from .items import Item
from .player import Player

def main():
    print("Welcome to Space Adventure!")
    rooms = setup_rooms()
    player = Player(rooms['Bridge'])
    
    while True:
        print(f"\n{player.current_room}")
        command = input("What do you do? ").strip().lower()
        if command in ("quit", "exit"): 
            print("Thanks for playing!")
            break
        elif command.startswith("go "):
            direction = command[3:]
            player.move(direction)
        elif command.startswith("take "):
            item_name = command[5:]
            player.take(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            player.use(item_name)
        elif command == "inventory":
            player.show_inventory()
        else:
            print("I don't understand that command.")
