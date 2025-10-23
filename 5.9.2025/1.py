def change():
    city = "Vantaa"
    print("At the end of the function: " + city)
    return
city = "Helsinki"
print("At the beginning of main program: " + city)
change()
print("At the end of main program: " + city)