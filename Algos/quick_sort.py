def quick_sort(nums, low, high):
    if low < high:
        i = partition(nums, low, high)
        quick_sort(nums, low, i - 1)
        quick_sort(nums, i + 1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i
# Psuedocode

#     Select a "pivot" element - We'll arbitrarily choose the last element in the list
#     Move through all the elements in the list and swap them around until all the numbers less than the pivot are on the left, and the numbers greater than the pivot are on the right
#     Move the pivot between the two sections where it belongs
#     recursively repeat for both sections
