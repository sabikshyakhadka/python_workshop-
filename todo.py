class todolist:
    
INVENTORY_FILE = "inventory.txt"
LEADERBOARD_FILE = "leaderboard.txt"

    def __init__(self):
        self.tasks = []
    def add_tasks(self, task):
        self.tasks.append(task)
        print(f"task '{task}'added to the list.")


    save_to_file(INVENTORY_FILE, todo_list)
    return todolist

def load_from_file(filename):
    """Load data from a file."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file]
    
def display_inventory():
    """Display the leaderboard."""
    leaderboard = load_from_file(LEADERBOARD_FILE)
    if leaderboard:
        print("\nLeaderboard:")
        for entry in leaderboard:
            print(entry)
    else:
        print("\nNo entries in the leaderboard yet.")

def update_leaderboard(todo _list, ):
    """Update the leaderboard."""
    save_to_file(LEADERBOARD_FILE, f"{player_name}: {score}")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"task'{task}'removed from the list.")
        else: 
            print(f"task'{task}'not found in the list.")

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self. tasks.index(old_task)
            self.tasks[index] = new_task
            print(f"task updateed to '{new_task}'.")
        
        else:
            print(f"task'{old_task}' not found in the list ")
    def show_tasks(self):
        if self.tasks:
            print ("your todo list:")
            for index, task in enumerate (self.tasks):
                print(f"{index + 1}.{task}")

        else:
            print("empty.")



todo_list = todolist()
            
todo_list.add_tasks("buy the things")
todo_list.add_tasks("finish the assignment")
todo_list.add_tasks("blacklist noy")

todo_list.show_tasks()
todo_list.remove_task("finish the assignment")
todo_list.update_task("buy the things", "go for the long drive")
todo_list.show_tasks()




