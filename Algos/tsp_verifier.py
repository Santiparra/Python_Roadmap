def verify_tsp(paths, dist, actual_path):
    total = 0
    for i in range(len(actual_path)):
        if i != 0:
            total += paths[actual_path[i - 1]][actual_path[i]]
    return total < dist
    
# Pseudocode

# Inputs:

#     paths: A matrix where each point represents the distance between the two cities. For example, paths[cityA][cityB] holds the distance from cityA to cityB. paths[cityA][cityB] = paths[cityB][cityA]
#     dist: The distance we are trying to find a path shorter than
#     actual_path: The path we are trying to verify

# Algorithm:

#     Loop over each city in the actual path
#     Sum the distance between each city in the actual path
#     If the sum is less than dist, return True, otherwise return False
