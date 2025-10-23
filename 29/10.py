grocery_list = ["milk", "bread", "eggs", "cheese", "apples"]
while grocery_list:
    item = input("Enter an item you bought: ")
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} is not on the list.")
    print("Remaining items:", grocery_list)