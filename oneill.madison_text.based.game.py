import random

# Game data
rooms = {
    'outside': {'name': 'Outside', 'north': 'dining room',
                'text': 'You are outside and stare at the back door to the house.'},

    'dining room': {'name': 'Dining Room', 'north': 'living room', 'west': 'kitchen',
                    'contents': {'vase': 50, 'painting': 100},
                    'text': 'You are in the dining room. \n'
                            'The kitchen is to your left and the living room is in front of you.'},

    'kitchen': {'name': 'Kitchen', 'east': 'dining room', 'contents': {'blender': 20, 'microwave': 30},
                'text': 'You are in the kitchen. \n'
                        'The dining room is to your right.'},

    'living room': {'name': 'Living Room', 'south': 'dining room', 'east': 'stairs', 'west': 'bathroom',
                    'contents': {'tv': 80, 'sofa': 70},
                    'text': 'You are in the living room. \n'
                            'The dining room is behind you, and there is a bathroom to your left and stairs to your '
                            'right.'},

    'bathroom': {'name': 'Bathroom', 'east': 'living room', 'contents': {'candle': 10, 'shampoo': 15},
                 'text': 'You are in the bathroom. \n'
                         'The living room is to your right.'},

    'stairs': {'name': 'Stairs', 'north': 'hallway', 'west': 'living room',
               'text': 'You are in the stairway. There is a hallway at the top that stretches out straight in front '
                       'of you.'},

    'hallway': {'name': 'Hallway', 'west': 'bedroom', 'east': 'kids bedroom',
                'text': 'You are in the hallway. There are bedrooms on either side of you.'},

    'bedroom': {'name': 'Bedroom', 'east': 'hallway', 'contents': {'jewelry': 70, 'watch': 50},
                'text': 'You are in the bedroom. \n'
                        'The hallway is to your right.'},

    'kids bedroom': {'name': 'Kids Bedroom', 'west': 'hallway', 'contents': {'musicbox': 40, 'teddy bear': 25},
                     'text': 'You are in a kids bedroom. \n'
                             'The hallway is to your left.'},
}

# Constants
DIRECTIONS = ['north', 'south', 'east', 'west']
ESCAPE_OPTIONS = ['window', 'front door']

# Global variables
currentRoom = rooms['outside']
carrying = []
police_location = random.choice(ESCAPE_OPTIONS)
time_limit = random.randint(10, 20)
time_spent = 0

def update_room_description(room):
    """Update room description to include contents if present."""
    description = room['text']
    if 'contents' in room and room['contents']:
        contents = ', '.join(room['contents'].keys())
        description += f" You see: {contents}."
    return description

def display_intro():
    """Display game introduction."""
    print('You never meant to turn to this life, but sometimes to make a living you have to do some dirty jobs.\n'
          'Steal as many objects as you can and escape without being caught by the police. \n'
          'Use directions north, south, east, and west to navigate your way through a home. '
          'The command "steal [object name]" will add the item to your duffle bag. Collect everything before the cops '
          'arrive. \n'
          'Enter "escape" at any time to escape the house with your bag. '
          'Be careful which way you choose, though, the police are on their way... fast!')

def move_player(command):
    """Handle player movement."""
    global currentRoom
    if command in currentRoom:
        currentRoom = rooms[currentRoom[command]]
    else:
        print("You can't go that way.")

def steal_item(command):
    """Handle stealing items from a room."""
    global carrying
    item = command.split()[1]
    if item in carrying:
        print('You already stole this item!')
    elif item in currentRoom.get('contents', {}):
        carrying.append(item)
        print(f'You stole the {item}!')
        currentRoom['contents'] = {}  # Remove all items from the room's contents
    else:
        print('That object is not in this room.')

def check_escape(command):
    """Handle escape attempt."""
    if command == police_location:
        print('The police are here! You are caught!')
        print('Game over')
    else:
        print('You escaped!')
        if carrying:
            print(f'and you have successfully burglarized the house! You stole: {", ".join(carrying)}')
        else:
            print('but you have not successfully burglarized the house... better luck next time.')

def main():
    global time_spent
    display_intro()

    while True:
        # Check if time limit is reached
        if time_spent >= time_limit:
            print('The police have arrived! You are caught!')
            print('Game over')
            break

        # Display current location
        print()
        print(update_room_description(currentRoom))

        # Get input
        command = input('\nWhat next? ').strip().lower()  # Convert input to lowercase to avoid case sensitivity
        time_spent += 1

        # Movement
        if command in DIRECTIONS:
            move_player(command)

        # Steal items
        elif command.startswith('steal '):
            steal_item(command)

        # Quit game
        elif command in ('e', 'exit'):
            break

        # Escape option
        elif command == 'escape':
            print('You hear the sirens closing in. There is not much time. How do you escape?')
            print('Window or Front Door...?')

        # Escape
        elif command in ESCAPE_OPTIONS:
            check_escape(command)
            break

        else:
            print('Invalid command. Try again.')

if __name__ == "__main__":
    main()
