# Kyunghoon Lee

def menu_instructions():
    # Print title menu and instructions for player
    print('*Welcome to "Another Day in the Office"*')
    print("Collect all 6 of the management team's favorite things around the office.")
    print("Make sure you grab everything before heading to the first meeting of the day!")
    print("Movement commands: 'Go North', 'Go South', 'Go East', 'Go West'")
    print("Add an item to your inventory using Get 'item name'")
    print("Type 'exit' to quit at any time.")
    print("Please keep in mind, all commands are case-sensitive!")


def main():
    # Initialize dict linking rooms and items, no items in beginning or boss room
    rooms = {
        'Reception Area': {'North': 'Staff Offices', 'East': 'Hallway', 'South': 'Meeting Area', 'West': 'Logistics Room', 'item': 'None'},
        'Meeting Area': {'North': 'Reception Area', 'East': 'Conference Room', 'item': 'Laptop'},
        'Conference Room': {'West': 'Meeting Area'},    # MANAGER IS HERE
        'Logistics Room': {'East': 'Reception Area', 'item': 'Phone Charger'},
        'Hallway': {'West': 'Reception Area', 'North': 'Break Room', 'item': 'Employee Plaque'},
        'Break Room': {'South': 'Hallway', 'item': 'Banana'},
        'Staff Offices': {'South': 'Reception Area', 'East': "Manager's Office", 'item': "Receptionist's Mug"},
        "Manager's Office": {'West': 'Staff Offices', 'item': 'Fancy Pen'}
    }

    # Set starting room and direction commands, create blank inventory
    current_room = 'Reception Area'
    directions = ['Go North', 'Go South', 'Go East', 'Go West']
    inventory = []

    # Define player_status function within main() per rubric instructions
    def player_status():
        print('===================')
        print(f'You are in the {current_room}.')
        print(f'Inventory: {inventory}')
        print('===================')

    # Show player main menu and instructions
    menu_instructions()
    print()

    # Initialize gameplay loop
    while True:
        # Check success or fail state at final room
        if current_room == 'Conference Room':
            if len(inventory) == 6:
                print('You collected all the items, and even made it to the meeting on time.')
                print('Everyone is looking for their missing items, and you watch the chaos unfold.')
                print("Congratulations! Too bad it's only Monday...")
                break
            else:
                print("You weren't able to collect everything, and you ended up late to the meeting...")
                print("Your boss isn't happy. Safe to assume you won't be getting a bonus this year.")
                print('Thanks for playing, feel free to try again!')
                break
        # Display current room and inventory
        player_status()
        room_dict = rooms[current_room]
        # Check if an item is available in the current room
        if 'item' in room_dict:
            global current_item
            current_item = room_dict['item']
            if current_item not in inventory and current_item != 'None':
                print(f'You could take this {current_item}.')
            elif current_item in inventory or current_item == 'None':
                print("There's nothing worth taking here.")
        # Prompt player for input
        movement = input('What do you want to do?\n')
        if movement in directions:
            # Translate movement command to rooms dict value
            movement = movement.split()[1]
            if movement in rooms[current_room].keys():
                # Moves player in chosen direction, if move is valid
                current_room = rooms[current_room][movement]
                print(f'Moving to {current_room}...')
            else:
                # Notifies player of invalid direction
                print("You can't go that way, try again.")
        elif movement == 'exit':
            # Moves player to exit room
            current_room = 'exit'
            exit_prompt = input('You are in the exit room. Type exit again to quit.\n')
            # Asks player for exit confirmation
            if exit_prompt == 'exit':
                break
            else:
                # Returns player to Reception if they do not exit
                current_room = 'Reception'
        # If player tries to pick up an item
        elif movement[4:] == current_item and current_item != 'None':
            # Prevents duplicate item pickup
            if current_item in inventory:
                print(f"You've already got the {current_item}.")
            # Picks up item if available
            else:
                print(f'You sneak by, steal the {current_item}, and add it to your inventory.')
                inventory.append(current_item)
        else:
            # Checks if movement command is valid
            print('Invalid command, please try again.')


# Play the game
main()
