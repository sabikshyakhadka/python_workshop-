def setup_mission():
    print("setting up for the mission for you....")
    available_foods = [
    "apple",
    "banana",
    "pizza",
    "water bottle ",
    "chocolate",
    "grapes",
    "cherries",
    "burger", 
    "pestries",
    "macarons",
    "pasta",  
    ]
    available_crews = int(input("enter available_crews"))
    print("setup completed .....")
    return available_crews, available_foods
   

def alien_attack_game():
    print("welcome to Alien_Attack_Game")
    print("starting mission......")
    crews_number, foods = setup_mission()
    print(f"you have{crews_number} astronuts and food avaiable = {foods}")
    print("welcome to Alien_Attack_Game")
    print("starting mission......")
    print("WELLCOME TO MARS")
    
    print("mission completed")
alien_attack_game()