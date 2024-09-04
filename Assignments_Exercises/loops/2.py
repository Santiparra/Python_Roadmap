# Critical Hit

# Barbarian characters in Fantasy Quest have a chance to critically hit when using a flurry attack. If the ability critically hits, 
# then every single attack in the flurry does double damage. A flurry attack's final attack already did double damage to begin with,
# so if the ability is a critical hit, then the final attack does 4x the damage!

# Assignment

# In the calculate_flurry_crit function, write a loop that calculates and returns the total_damage of the flurry.

# The function takes 2 inputs num_attacks, base_damage.

#     Range over the num_attacks for the flurry
#     Calculate the total damage for each attack within the flurry. Remember, critical hits do double the base_damage!
#     The final swing of the flurry should do 4x the base_damage
#     Return the total damage

def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = ((num_attacks -1) * (base_damage *2)) + (base_damage * 4)                
        
    
    return total_damage

#OR

def calculate_flurry_crit(num_attacks, base_damage):
    total = 0
    for i in range(num_attacks):
        if i == num_attacks - 1:
            total += base_damage * 4
        else:
            total += base_damage * 2
    return total
