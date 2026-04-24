class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]
            if next_room.locked:
                if next_room.lock_item and any(item.name == next_room.lock_item for item in self.inventory):
                    print(f"You use the {next_room.lock_item} to unlock the door.")
                    next_room.locked = False
                else:
                    print("The door is locked.")
                    return
            self.current_room = next_room
            print(f"You move {direction}.")
        else:
            print("You can't go that way.")

    def take(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                self.inventory.append(item)
                self.current_room.items.remove(item)
                print(f"You take the {item_name}.")
                return
        print(f"There is no {item_name} here.")

    def use(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                print(f"You use the {item_name}. (Nothing happens... yet)")
                return
        print(f"You don't have a {item_name}.")

    def show_inventory(self):
        if self.inventory:
            print("You have:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")
