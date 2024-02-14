class Item(object):
    def __init__(self, name, description, is_movable):
        self.name = name
        self.description = description
        self.is_movable = is_movable

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

class Player(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

#=========================================================================================================================================
# Items
#=========================================================================================================================================

#=========================================================================================================================================
# Locations
#=========================================================================================================================================

#=========================================================================================================================================
# Player
#=========================================================================================================================================

player = Player("The Player", None)

#=========================================================================================================================================
# Gameplay Loop
#=========================================================================================================================================

while True:
    print("")
    print(player.location.name)
    print(player.location.description)
    print("\nHere are the exits: ")
    for exit in player.location.exits:
        print(exit)
    print("\nYou see the following: ")
    for item in player.location.items:
        print(item.name)
        
    # Get command
    try:
        # Python 2.7
        command = raw_input("\n> ")
    except:
        # Python 3.x
        command = input("\n> ")
        
    words = command.split()
    if len(words) > 0:
        verb = words[0]
    if len(words) > 1:
        noun = words[1]
    
    # Examine
    if verb == "examine":
        for item in player.location.items:
            if item.name == noun:
                print(item.description)
        for item in player.inventory:
            if item.name == noun:
                print(item.description)

    # Get
    if verb == "get":
        for item in player.location.items:
            if item.name == noun:
                # Check is it movable
                if item.is_movable:
                    print("You take the {}".format(item.name))
                    # Remove from room
                    player.location.items.remove(item)
                    # Add to player's inventory
                    player.inventory.append(item)
                
                else:
                    print("Sorry, you can't move that.")

    # Drop
    if verb == "drop":
        for item in player.inventory:
            print("You drop the {}.".format(item.name))
            player.inventory.remove(item)
            player.location.items.append(item)
        
    # Inventory
    if verb in ["inv", "inventory"]:
        print("You have the following: ")
        for item in player.inventory:
            print(item.name)

    # Movement
    if verb in ["n", "s", "e", "w", "u", "d"]:
        if verb in player.location.exits:
            player.location = player.location.exits[verb]
            print("You go {} and find yourself in a new room.".format(verb))