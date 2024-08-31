#We are going to design a program
# that determines how long a microwave oven at a sandwich shop will run.

#small = 30 sec
#medium = 60 sec
#large = 1 min and 15s
#extra large = 2 min and 15s


#User input
small = int(input("Enter the number of small sandwiches: "))
medium = int(input("Enter the number of medium sandwiches: "))
large = int(input("Enter the number of large sandwiches: "))
extra_large = int(input("Enter the number of extra-large sandwiches:"))

##calculations
small_time = 30 * small
medium_time = 60 * medium
large_time = 75 * large
extra_large_time = 135 * extra_large

total_time_general = small_time + medium_time + large_time + extra_large_time

total_time_min = int(total_time_general) //60
total_time_sec = int(total_time_general) % 60

##output
print(f"\nYou've entered {small} small sandwiches.")
print(f"You've entered {medium} medium sandwiches.")
print(f"You've entered {large} large sandwiches.")
print(f"You've entered {extra_large} extra-large sandwiches.")


print(f"\nTotal cooking time is {total_time_min} minutes and {total_time_sec} seconds.")


