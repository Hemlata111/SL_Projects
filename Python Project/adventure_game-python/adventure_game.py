#Task 1: Set up the project
    # Actions:
        # Open VS Code and create a new folder for your project
        # Inside the folder, create a new Python file named adventure_game.py
        # Add an inline comment to describe the purpose of the script
        # Run a simple print statement to confirm that the setup is working

#----------------------------------------------------------------------------
# Adventure Game - A simple text-based adventure game where players explore and search for treasure
#----------------------------------------------------------------------------
    
# Task 2: Create a function to start the game
    # Actions:
        # Define the function start_game() to display the game introduction
        # Ask the player for their name and store it in a variable
        # Provide the player with an initial choice (explore a forest or enter a cave)

def start_game():
    """Start the adventure game"""
    print("\n=== The Legendary Treasure Hunt ===\n")
    print("Welcome to your adventure! You'll explore an ancient land in search of treasure.")
    print("Your choices will determine your fate. Choose wisely!\n")
    player_name = input("What is your name, adventurer? ")
    print(f"\nWelcome, {player_name}! Your adventure begins now!\n")
    
    print("You stand at a crossroads. Before you lie two paths:")
    print("1. A dark forest with ancient trees")
    print("2. A cave entrance in the mountain")
    
    choice = input("\nWhich path will you choose? (1/2): ")
    
    if choice == "1":
        return forest_path()
    elif choice == "2":
        return cave_path()
    else:
        print("Invalid choice. Please try again.")
        return start_game()

#---------------------------------------------------------------------------
# Task 3: Create the forest path
    # Actions:
        # Define the function forest_path() that describes the forest scenario
        # Provide the player with choices (follow a river or climb a tree)
        # Use an if-else structure to handle player choices   

def forest_path():
    """Handle the forest path scenario"""
    print("\nYou enter the forest. The trees are tall and the air is fresh.")
    print("You see a river flowing nearby and a tall tree that looks climbable.")
    
    choice = input("Do you want to 'follow the river' or 'climb the tree'? ").lower()
    
    if "river" in choice:
        print("\nYou follow the river and discover a beautiful waterfall.")
        print("Behind it, you find a hidden cave with ancient treasure!")
        return "win"
    elif "tree" in choice:
        print("\nYou climb the tree but slip and fall.")
        print("You must return home to recover.")
        return "lose"
    else:
        print("That's not a valid choice. Try again.")
        return forest_path()

#---------------------------------------------------------------------------
# Task 4: Create the cave path
# Actions:
    # Define the function cave_path() that describes the cave scenario
    # Provide the player with choices (light a torch or proceed in the dark)
    # Use conditionals to determine the outcome

def cave_path():
    """Handle the cave path scenario"""
    print("\nYou enter the cave. It's dark and you can hear dripping water.")
    choice = input("Do you want to 'light a torch' or 'proceed in dark'? ").lower()
    
    if "torch" in choice:
        print("\nYou light the torch and find ancient wall paintings.")
        print("They lead you to a chamber with legendary treasure!")
        return "win"
    elif "dark" in choice:
        print("\nYou stumble in the darkness and fall into a pit.")
        print("Your adventure ends here.")
        return "lose"
    else:
        print("That's not a valid choice. Try again.")
        return cave_path()

#---------------------------------------------------------------------------
# Task 5: Run the adventure game
# Actions:
    # Call start_game() to begin the adventure
    # Ensure the program runs in a loop until the player completes their journey
    # Provide an option to restart the game after completion

def main():
    """Main game loop"""
    while True:
        result = start_game()
        
        if result == "win":
            print("\nCongratulations! You've found the legendary treasure!")
        else:
            print("\nGame Over! Better luck next time!")
            
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    print("\nThank you for playing!")

if __name__ == "__main__":
    main()
