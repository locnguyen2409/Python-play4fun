user_list = []
while True:
    user_input = input("New item(0 to exit): ")
    try:
        number = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue
    if number == 0:
        print("Bye!")
        break

    user_list.append(number)
    print(f"The list now: {user_list}")
    sorted_list = sorted(user_list)
    print(f"The list in order: {sorted_list}")
