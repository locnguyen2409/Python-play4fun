import random
def scavenge_fuel(success_chance=0.7, fuel_reward=10):
    print("\nScavenging for fuel...")
    if random.random() < success_chance:
        print(f" Success! You found {fuel_reward} units of fuel.")
        return fuel_reward
    else:
        print(" No fuel found.")
        return 0

def play_one_attempt_game():
    print(" Welcome to the One-Shot Fuel Scavenger!")
    name = input("Enter your name, survivor: ")

    input("\nPress Enter to make your one and only scavenging attempt...")

    fuel_collected = scavenge_fuel()

    print(f"\n{name}, you collected  {fuel_collected} units of fuel.")
    if fuel_collected >= 10:
        print(" That's enough to move forward!")
    else:
        print(" You’ll have to try again next time...")

play_one_attempt_game()