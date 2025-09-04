import random

num_dice = int(input("How many dice do you want to roll? "))
if num_dice <= 0:
    print("Please enter a number greater than zero.")
else:
    total_sum = 0
    print("Rolling the dice...")
    for i in range(num_dice):
        roll = random.randint(1, 6)
        print(f"Roll #{i + 1}: {roll}")  # Optional: show each roll
        total_sum += roll
    print(f"\nThe sum of all rolls is: {total_sum}")