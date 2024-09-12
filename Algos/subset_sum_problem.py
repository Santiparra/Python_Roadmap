def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(nums) -1)


def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    if index < 0 and target != 0:
        return False
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    result = find_subset_sum(nums, target, index -1)
    result2 = find_subset_sum(nums, target -nums[index], index -1 )
    return result or result2
    
# Pseudocode: subset_sum(nums, target)
# Inputs

#     nums: A list of integers representing the follower counts of influencers.
#     target: The target sum we want to find a subset for.

# Output

# True if there exists a subset of nums that adds up to target. False otherwise.
# Algorithm

#     Call the helper function starting with the last index in nums and return its result.

# Pseudocode: find_subset_sum(nums, target, index)
# Inputs

#     nums: A list of integers representing the follower counts of influencers.
#     target: The target sum we want to find a subset for.
#     index: The index of the current element we're considering.

# Output

# True if there exists a subset of nums that adds up to target. False otherwise.
# Algorithm

#     If the target is 0, return True.
#     If the index is less than 0 and the target is not 0, return False.
#     If the number at the current index is greater than the target, call the helper function with the same target but with the index decremented by 1, and return the result, we're done.
#     Otherwise, call the helper function with the same target and index decremented by 1, and save the result.
#     Also, call the helper function with the target reduced by the value of the current element and the index decremented by 1
#     If either of these calls returns True, return True. Otherwise, return False.
