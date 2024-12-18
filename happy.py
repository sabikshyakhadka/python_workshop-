batteries = (50, 30, 4, 45, 12, 18, 30)
mininum_battery_power = 29 
usable_battery_power = 0 
usable_battery_count = 0
for battery in batteries:
    if battery > mininum_battery_power:
        usable_battery_power += battery
        usable_batter_count = usable_battery_count + 1 
print (f"there are {usable_battery_count} batteries which can be used to genetrate {usable_battery_power}")
