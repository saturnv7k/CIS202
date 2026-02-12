#input (avg speed, speed limit, and distance traveled)
average_speed = float(input("Enter your average speed (mph): "))
speed_limit = float(input("Enter the posted speed limit (mph): "))
tot_distance = float(input("Enter the total distance travelled (miles): "))

#calculating input values
time_following_limit = tot_distance / speed_limit
time_if_speeding = tot_distance / average_speed
time_saved_minutes = (time_following_limit - time_if_speeding) * 60

#output
if time_saved_minutes <= 0:
    print("You did not save any time.")
else:
    print(f'You saved {time_saved_minutes} minutes.')
