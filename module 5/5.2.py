numbers = []

while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == "done":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

numbers.sort(reverse=True)
top_five = numbers[:5]

print("The five greatest numbers are:")
for num in top_five:
    print(num)