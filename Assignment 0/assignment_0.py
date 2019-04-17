"""
CIS 41A - Assignment 0
Name: David Rios
Date: 4-9-19
"""

from math import pi

# The Volume Question (#1)
radius = 5
sphere_volume = (4/3)*pi*(radius**3)
print("The Sphere Volume is {}".format(sphere_volume))

# The Shipping Question (#2)
base_shipping = 3
per_unit_shipping = 0.75
discounted_price = 0.6
price = 25.95
qty = 60

# Calculate shipping cost. (#2)
shipping = base_shipping + (qty - 1)*per_unit_shipping
# Rounding the book price, adding shipping.
total = round((price*discounted_price)*qty + shipping, 2)
# Print cost of the books, to two decimal places.
print("\nThe total cost for {} books is: ${:.2f}".format(qty, total))


# The Pace Question (#3)

hour = 6
minute = 52

easy_pace = (8*60)+15  # Calculates the easy pace.
tempo_pace = (7*60)+12  # Calculates the tempo pace.
# Calculating out the start time in minutes.
starttime = (hour*60)+minute
# Calculating pace time as a whole, incl. easy & tempo.
pacetime = ((easy_pace*2)+(3*tempo_pace))/60
totaltime = pacetime + starttime

time = totaltime // 60, totaltime % 60  # Completion time, set to a tuple.

# Formats total time in hours:minutes
totaltime = '{}:{}'.format(int(time[0]), round(time[1]), 0)

print('\nYou will finish at {}'.format(totaltime))  # Prints it all out
