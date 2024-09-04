# Match Countdown

# We need a timer to countdown the start of PvP matches in Fantasy Quest.
# Assignment

# In the countdown_to_start function, write a loop that counts down from 10 to 1. At each iteration, print the number with an ellipsis:

# i...

# However, when i is 1, it should print 1...Fight! instead.
def countdown_to_start():
    for i in range(10, 0, -1):
        if i == 1:
            print(f"{i}...Fight!")
        else:
            print(f"{i}...")

#OR

def countdown_to_start():
    countdown = 10
    while countdown > 1:
        print(f"{countdown}...")
        countdown -= 1
    print(f'{countdown}...Fight!')  