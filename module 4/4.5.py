attempts = 0
while attempts < 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "python" and password == "rules":
        print("Welcome!")
        break
    else:
        attempts += 1
        print(f"Incorrect credentials. You have {5 - attempts} attempts left.")
    if attempts == 5:
        print("Access denied!")