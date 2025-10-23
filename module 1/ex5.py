talents=float(input("Enter the talents: "))
pounds=float(input("Enter the pounds: "))
lots=float(input("Enter the lots: "))
weight=((talents*20+pounds)*32+lots)*13.3
weight_kg=int(weight/1000)
weight_gr=weight%1000
print("The weight in modern units: ",weight_kg, f"kilograms: {weight_kg} and {weight_gr:.2f} grams")
