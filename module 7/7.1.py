season = ("winter", "spring", "summer", "autumn")
month = int(input("Month number (1-12): "))
if month in [12,1,2]:
    print(season[0])
elif month in [3,4,5]:
    print(season[1])
elif month in [6,7,8]:
    print(season[2])
elif month in [9,10,11]:
    print(season[3])
else:
    print("Invalid month number!")