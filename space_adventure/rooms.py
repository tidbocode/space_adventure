class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.locked = False
        self.lock_item = None

    def connect(self, direction, room, locked=False, lock_item=None):
        self.exits[direction] = room
        if locked:
            room.locked = True
            room.lock_item = lock_item

    def __str__(self):
        desc = f"{self.name}\n{self.description}\n"
        if self.items:
            desc += "You see: " + ", ".join(item.name for item in self.items) + "\n"
        desc += "Exits: " + ", ".join(self.exits.keys())
        return desc

def setup_rooms():
    bridge = Room("Bridge", "The command center of your spaceship. Flickering screens show warnings.")
    airlock = Room("Airlock", "A small chamber with a suit locker. The exit to space is locked.")
    engine = Room("Engine Room", "The engine hums quietly. There is a toolbox here.")

    bridge.connect("south", airlock)
    airlock.connect("north", bridge)
    bridge.connect("east", engine, locked=True, lock_item="keycard")
    engine.connect("west", bridge)

    from .items import Item
    keycard = Item("keycard", "A plastic card with a magnetic strip.")
    suit = Item("spacesuit", "A suit for spacewalks.")
    toolbox = Item("toolbox", "A box of assorted tools.")

    airlock.items.append(suit)
    bridge.items.append(keycard)
    engine.items.append(toolbox)

    return {"Bridge": bridge, "Airlock": airlock, "Engine Room": engine}
