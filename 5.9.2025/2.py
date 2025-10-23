def greet( greeting, times):
    for i in range(times):
        print(greeting + " round: " + str(i+1))
    return
greet(greeting="Hello", times=3)
a = input("Enter the greeting wish to be printed: ")
b = int(input("Enter the number ò time you wish to make iterations: "))
greet(a,b)

