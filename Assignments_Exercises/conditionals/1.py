# Mount Rental

# We are adding a new feature to Fantasy Quest that allows characters to rent mounts for a short period of time. 
# The character must return the mount before they have used up all their time otherwise they are charged an overtime fee of additional gold.
# Assignment

# Write the check_mount_rental function. It takes two inputs:

#     time_used - the amount of time the mount has been used in minutes
#     time_purchased - the amount of time the character rented the mount for

#     If time_used meets or exceeds time_purchased, then the rental is expired and the function should return the string "overtime charged"
#     Otherwise, return the string "no charges yet"

# Bonus: Try to accomplish this without an "else" statement.

def check_mount_rental(time_used, time_purchased): 
    if time_used >= time_purchased:
        return "overtime charged"
    return "no charges yet"