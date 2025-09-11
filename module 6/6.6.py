import math

def unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 100) / 2
    area_m2 = math.pi * radius_m ** 2
    return price_eur / area_m2

def main():
    print("Enter details for Pizza 1:")
    d1 = float(input("Diameter in cm: "))
    p1 = float(input("Price in euros: "))

    print("\nEnter details for Pizza 2:")
    d2 = float(input("Diameter in cm: "))
    p2 = float(input("Price in euros: "))

    unit1 = unit_price(d1, p1)
    unit2 = unit_price(d2, p2)

    print(f"\nPizza 1 unit price: {unit1:.2f} €/m²")
    print(f"Pizza 2 unit price: {unit2:.2f} €/m²")

    if unit1 < unit2:
        print("Pizza 1 offers better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 offers better value for money.")
    else:
        print("Both pizzas offer the same value for money.")

main()
