# Evens and odds

# You've been asked to write a program that will calculate how many odd and even numbers exist in a list.
# Challenge

# Write the get_odds_and_evens function to loop through the numbers list and check if each number in the list is either odd or even.

# Increment the num_evens counter if even, and the num_odds counter if it's odd. Lastly, return the two values num_odds and num_evens in that order.
# Tip

# Remember, you can check if a number is divisible by another number using the modulo operator (%) and comparing the result.

# def divisible_by_5(num):
#     return num % 5 == 0


# print(divisible_by_5(20))
# # True
# print(divisible_by_5(19))
# # False
def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0

    for number in numbers:
        if number % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1 

    return num_odds, num_evens
