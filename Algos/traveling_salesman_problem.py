def tsp(cities, paths, dist):
    perms = permutations(cities)
    for perm in perms:
        total_dist = 0
        for i in range(1, len(perm)):
            total_dist += paths[perm[i - 1]][perm[i]]
        if total_dist < dist:
            return True
    return False

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res

def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

# Pseudocode

# Inputs:

#     cities: A list of city identifiers (integers 0-n)
#     paths: A matrix where each point represents the distance between the two cities. For example, paths[cityA][cityB] holds the distance from cityA to cityB. paths[cityA][cityB] = paths[cityB][cityA]
#     dist: The distance we are trying to beat

# Algorithm:

#     Use the permutations function to get the matrix of all possible paths through the given cities. Where the first path, [1, 2, 3] represents moving from city 1 -> city 2 -> city 3
#     Iterate over each possible path (permutation)
#         Sum the distances between each city in the path using the paths matrix to look up the distances
#         If the total distance of the path is less than the given dist return True
#     If no short paths were found, return False
