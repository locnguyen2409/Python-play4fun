largest = 0
smallest = 0
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        if largest == 0 or largest < num:
            largest = num
        elif smallest == 0 or smallest > num:
            smallest = num
    except:
        print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)
