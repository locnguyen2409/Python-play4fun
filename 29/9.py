colors = ["red", "green", "yellow", "blue", "white"]
print("What is your favourite color?")
color = input()
if color in colors and color != "red":
    print("It is in the list but not my favourite color.")
elif color == "red":
    print("My favourite color is red")
elif color not in colors:
    print("Wrong color")
print("Goodbye!")