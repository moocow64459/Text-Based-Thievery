import random

rooms = {
    'Outside': {'name': 'Outside', 'north': 'Dining Room',
                'text': 'You are outside and stare at the back door to the house.'},

    'Dining Room': {'name': 'Dining Room', 'north': 'Living Room', 'west': 'Kitchen',
                    'contents': {'vase': 50, 'painting': 100},
                    'West': 'Kitchen',
                    'text': 'You are in the dining room. There is a vase and a painting in this room... They look '
                            'valuable.\n'
                            'The kitchen to your left and the living room is in front of you.'},

    'Kitchen': {'name': 'Kitchen', 'east': 'Dining Room', 'contents': {'blender': 20, 'microwave': 30},
                'text': 'You are in the kitchen. There is a blender and a microwave on the counter.\n'
                        'The dining room is to your right.'},

    'Living Room': {'name': 'Living Room', 'south': 'Dining Room', 'east': 'Stairs', 'west': 'Bathroom',
                    'contents': {'tv': 80, 'sofa': 70},
                    'text': 'You are in the Living room. There is a tv on the wall and a sofa.\n'
                            'The dining room is behind you and there is a bathroom to your left and stairs to your '
                            'right.'},

    'Bathroom': {'name': 'Bathroom', 'east': 'Living Room', 'contents': {'candle': 10, 'shampoo': 15},
                 'text': 'You are in the Bathroom. There is a candle on the counter and a bottle of shampoo.\n'
                         'The living room is to your right.'},

    'Stairs': {'name': 'Stairs', 'north': 'Hallway', 'west': 'Living Room',
               'text': 'You are in the stairway. There is a hallway at the top that stretches out straight in front '
                       'of you.'},

    'Hallway': {'name': 'Hallway', 'west': 'Bedroom', 'east': 'Kids Bedroom',
                'text': 'You are in the hallway. There are bedrooms on either side of you.'},

    'Bedroom': {'name': 'Bedroom', 'east': 'Hallway', 'contents': {'jewelry': 70, 'watch': 50},
                'text': 'You are in the bedroom. There is jewelry on the dresser and a watch.\n'
                        'The hallway is to your right.'},

    'Kids Bedroom': {'name': 'Kids Bedroom', 'west': 'Hallway', 'contents': {'musicbox': 40, 'teddy bear': 25},
                     'text': 'You are in a kids bedroom. There is a musicbox on a shelf and a teddy bear.\n'
                             'The hallway is to your left.'},
}

directions = ['north', 'south', 'east', 'west']
currentRoom = rooms['Outside']
carrying = []
escape = ['escape', 'Escape']
escape_window = ['window']
escape_fd = ['front door']  # villain

# instructions/intro
print('You never meant to turn to this life, but sometimes to make a living you have to do some dirty jobs.\n'
      'Steal as many objects as you can and escape without being caught by the police. \n'
      'Use directions north, south, east, and west to navigate your way through a home. '
      'The command \"steal [object name]\" will add the item to your duffle bag. Collect everything before the cops '
      'arrive. \n'
      'Enter \'escape\' at any time to escape the house with your bag. '
      'Be careful which way you choose, though, the police are on their way... fast!')

while True:

    # display current location
    print()
    print(format(currentRoom['text']))
    # get input
    command = input('\nWhat next? ').strip().lower()  # convert input to lowercase to avoid case sensitivity

    # movement
    if command in directions:
        if command in currentRoom:
            currentRoom = rooms[currentRoom[command]]
        else:
            print("You can't go that way.")

    # get objects
    elif command.split()[0] == 'steal':
        item = command.split()[1]
        if item in carrying:
            print('You already stole this item!')

        elif item in currentRoom['contents']:
            if isinstance(currentRoom['contents'][item], dict):
                print(f'There are multiple items in this room: {list(currentRoom["contents"].keys())}.')
                choice = input('Which item do you want to steal? ').strip().lower()
                if choice in currentRoom['contents']:
                    carrying.append(choice)
                    print(f'You stole the {choice}!')
                    del currentRoom['contents'][choice]  # Remove the stolen item from the room's contents
                else:
                    print('Invalid choice.')
            else:
                carrying.append(item)
                print(f'You stole the {item}!')
                del currentRoom['contents'][item]  # Remove the stolen item from the room's contents
        else:
            print('That object is not in this room.')

    # quit game
    elif command in ('e', 'exit'):
        break

    # exit option
    elif command in escape:
        print('You hear the sirens closing in. There is not much time. How do you escape?')
        print('Window or Front Door...?')

    # Escape
    elif command in escape_window:
        print('You escaped!')
        if len(carrying) == 6:
            print('and you have successfully burglarized the house!')
            break
        elif len(carrying) < 6:
            print('but you have not successfully burglarized the house... better luck next time.')
            break

    # Villain escape
    elif command in escape_fd:
        print('You were caught by the police!')
        print('game over')
        break
