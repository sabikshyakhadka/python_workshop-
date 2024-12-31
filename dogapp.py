import random
import time
import threading
import os

# Constants for file names
SAVE_FILE = "pet_save.TXT"

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def feed(self):
        self.hunger = min(self.hunger + 20, 80)
        print(f"{self.name} is being fed. Hunger level: {self.hunger}")

    def play(self):
        if self.energy > 0:
            self.happiness = min(self.happiness + 20, 80)
            self.energy = max(self.energy - 10, 0)
            print(f"{self.name} is playing. Happiness level: {self.happiness}, Energy level: {self.energy}")
        else:
            print(f"{self.name} is too tired to play.")

    def rest(self):
        self.energy = min(self.energy + 20, 80)
        self.hunger = max(self.hunger - 5, 0)
        print(f"{self.name} is resting. Energy level: {self.energy}, Hunger level: {self.hunger}")

    def status(self):
        print(f"Status of {self.name} - Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}")

    def check_sickness(self):
        return self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0

    def check_win(self, win_streak):
        return self.hunger > 80 and self.happiness > 80 and self.energy > 80 and win_streak >= 3

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        pet = Pet(data['name'])
        pet.__dict__.update(data)
        return pet

def save_game(pet):
    with open(SAVE_FILE, 'w') as file:
        json.dump(pet.to_dict(), file)
    print("Game saved.")

def load_game():
    if not os.path.exists(SAVE_FILE):
        return None
    with open(SAVE_FILE, 'r') as file:
        data = json.load(file)
    return Pet.from_dict(data)

def countdown(time_sec):
    while time_sec > 0:
        time.sleep(1)
        time_sec -= 1
    print("\nTime's up!")

def random_event(pet):
    events = ["finds a toy", "loses a toy", "finds food", "gets scared"]
    event = random.choice(events)
    if event == "finds a toy":
        pet.happiness = min(pet.happiness + 10, 80)
        print(f"{pet.name} found a toy! Happiness level: {pet.happiness}")
    elif event == "loses a toy":
        pet.happiness = max(pet.happiness - 10, 0)
        print(f"{pet.name} lost a toy! Happiness level: {pet.happiness}")
    elif event == "finds food":
        pet.hunger = min(pet.hunger + 10, 80)
        print(f"{pet.name} found some food! Hunger level: {pet.hunger}")
    elif event == "gets scared":
        pet.happiness = max(pet.happiness - 10, 0)
        pet.energy = max(pet.energy - 10, 0)
        print(f"{pet.name} got scared! Happiness level: {pet.happiness}, Energy level: {pet.energy}")

def pet_game():
    pet = load_game()
    if pet is None:
        name = input("What is the name of your pet? ")
        pet = Pet(name)
        print("\nStarting a new adventure...")
    else:
        print("\nResuming your adventure...")

    win_streak = 0
    while True:
        pet.status()
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Rest")
        print("4. Save and Exit")
        
        timer_thread = threading.Thread(target=countdown, args=(10,))
        timer_thread.start()
        action = input("Enter your choice (1/2/3/4): ").strip()
        timer_thread.join()  # Wait for the timer to finish

        if action == "1":
            pet.feed()
        elif action == "2":
            pet.play()
        elif action == "3":
            pet.rest()
        elif action == "4":
            save_game(pet)
            print(f"\nThanks for playing! Your pet {pet.name} will be waiting for you.")
            break
        else:
            print("Invalid choice. Please try again.")

        if random.random() < 0.3:  # 30% chance for a random event
            random_event(pet)

        if pet.check_sickness():
            print(f"{pet.name} got sick. Game over!")
            break

        if pet.hunger > 80 and pet.happiness > 80 and pet.energy > 80:
            win_streak += 1
        else:
            win_streak = 0

        if pet.check_win(win_streak):
            print(f"{pet.name} is super happy and energetic! You win!")
            break

if __name__ == "__main__":
    pet_game()