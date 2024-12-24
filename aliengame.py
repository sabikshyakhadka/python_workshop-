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
def get_charged_batteries():
    batteries = (50, 30, 4, 45, 12, 18, 30)
    mininum_battery_power = 20 
    usable_battery_power = 0 
    usable_battery_count = 0
    for battery in batteries:
        if battery > mininum_battery_power:
            usable_battery_power += battery
            usable_batter_count = usable_battery_count + 1 
            if usable_battery_power >= 100:
                return usable_battery_power, usable_battery_count
       
def decrypt_alien_message(alien_message):
    human_message = alien_message [::-1]
    return human_message

def food_divide_equally(food, crews_number):
    equally_food = len(food)// crews_number
    remaning_food_count = len(food) % crews_number
    return equally_food, remaning_food
def alien_attack_game():
    print("welcome to Alien_Attack_Game")
    print("starting mission......")

    crews_number, food = setup_mission()
    print(f"you have{crews_number} astronuts and food avaiable = {food}")

    print("welcome to Alien_Attack_Game")
    print("starting mission......")
    print("WELLCOME TO MARS")
    print("the battery is dead please change the battery")
    battery_power, battery_count = get_charged_batteries()
    print("hurry!!! your battery is charged")
    print("opps... alien has arrived and they have send message to you")
    print("rednerrus")
    
    decrypt_text = decrypt_alien_message("rednerrus")
    print (f"alien is saying : {decrypt_text}")
    print ("alien has captured all astronouts")
    print("if astronouts wants to escape they have to divide each food and give remaning foods")

    food_divide_equally(food, crews_number)
    print(f"you have {equally_divided} food divided equally and remaning = {remaning_food}")
    print ("okay... now you can go to earth ")
    print("mission completed")
alien_attack_game()