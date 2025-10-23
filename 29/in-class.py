a = float(input("Enter hourly wage: "))
b = float(input("Enter hours worked: "))
c = input("Enter day of a week: ")
if c == "sunday":
    a *= 2
daily_wage = a * b
print(f"Daily wages: {daily_wage} euros")



command = input("Enter command: ")
while command != "quit":
    print("We are free, let's"+ command)
    command = input("Enter command: ")
print ("Execution stopped explicitly")



first = 2
while first == 2:
    second = 1
    while second <= 20:
        print(f"{first} times {second} is {first * second:d}")
        second = second + 1