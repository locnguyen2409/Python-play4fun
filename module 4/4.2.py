while True:
    inches = float(input("Enter inches (negative to quit): "))

    if inches < 0:
        break

    centimeters = inches * 2.56
    print(f"{inches} inches = {centimeters:.2f} centimeters.")

print("Program ended.")