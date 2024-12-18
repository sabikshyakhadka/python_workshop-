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
available_crews = 3
each_crew_food = len(available_foods)// available_crews
remaning_food_count = len(available_foods) % available_crews 
print(f"each crew got {each_crew_food} food and remaning_food_count = {remaning_food_count}")
