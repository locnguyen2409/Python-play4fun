import random
secret_number = random.randint(1, 10)
while True:
    try:
        guess = int(input("Guess a number: "))
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print(f"Correct. The secret number is {secret_number}")
            break
    except:
        print("Invalid input")
