import random
import dateline
import os
import time
INVENTORY_FILE = "inventory.txt"
LEADERBOARD_FILE = "leaderboard_file"

def save_to_file(filename, date, mobe="a"):
    """save data to a file. """
    with opem(filename, mode) as file:
        file.write(data + " bv\n")

def explore_location():
    """explore a random location and find tresaure"""
    locations = ["mysterious cave", "hunted forest","deserted beach","ancient ruins"]
    treasure  = ["golder crow", ":silver sowrd","dimond necklace","ancient artifact"]
    
    location = random.choice(locations)
    treasure = random.choice(treasures)
    
    print(f"\nexploring {location}...")
    time.sleep(2)
    print(f"you found a {treasure}") 

    save_to_fil(INVENTORY_FILE, tresure)
    return treasure

def load_from_file(filename):
    """load data from a file"""
    if  not os.path.exists(filename):
        return[]
    with open(filename,"r") as file
        return[line.strip() for line in file]
def display_inventory():
    """ display the leaderboard."""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nleaderboard:")
        for entry in leaderboard :
            print(entry)
    else:
        print("\nNo entries in the leaderboard")
    save to file (INVENTORY_FILE, treasure)
def tresure_hunt():
    print("welcome to treasure hunt")
    player_name = input("enter your name: ").strip()
    if os.path.exists(INVENTORY_FILE):
        print("\nResuming your game..")
    else:
        print("\n strating the new game ") 
        open(INVENTORY_FILE, "W").close()
    score = 0 
    while True:
        print("\nwhat would you like do?")
        print("1. explore a new location")
        print("2. view inventory")
        print("3. quite and save the progress")
        choice = input("enter your choice(1/2/3): ").strip()
        if choice == "1":
            treasure = explore_location()
            score += 1
            print(f"you added {treasure} to your inventory ")
        elif choice == "2" :
            display inventory()
        elif choice == "3":
            print(f"\nthank you for palying {player_name}") 
            print(f"you have collected {score}")   
            print(f"Invalid choice.please try again.")
def display_leaderboard():
    """ display the leaderboard"""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nleaderboard:")
        for entry in leaderboard
        print(entry)
    else:
        print("\nNo entry in leaderboard yet:")
        b  
def view_Leaderboard():



def main():
    while True:
     print("\n== /tresure Hunt menu ==")
     print("1.start\Resume Game") 
     print("2. view Leaderboard")
     print("3. Exit ")
    choice = input("enter your choice (1/2/3): ").strip()
    if choice == "1":
        tresure_hunt()
    elif choice == "2":
        view Leaderboard()
    elif choice == "3":
        print("goodbye!")
if__name__== "__main__":
    main()
