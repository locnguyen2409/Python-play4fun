"""import mariadb
connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='baoloc123',
    database='people1',
    autocommit=True
)
print("Connection Successful")

import random

def update_fuel_level(connection, new_fuel, game_id):
    Update = 'UPDATE game SET fuel = %s WHERE id = %s'
    cursor = connection.cursor()
    try:
        cursor.execute(Update, (new_fuel, game_id))
        connection.commit()
        print("Fuel level updated.")
    except Exception as e:
        print("Fuel update failed:", e)

    Check = 'SELECT fuel FROM game WHERE id = %s'
    try:
        cursor.execute(Check, (game_id,))
        result = cursor.fetchone()
        if result:
            fuel_level = int(result[0])
            print(f"Current fuel level: {fuel_level}")
            return fuel_level
        else:
            print("No record found.")
            return None
    except Exception as e:
        print("Fuel check failed:", e)
        return None


def update_food_level(connection, new_food, game_id):
    Update = 'UPDATE game SET food = %s WHERE id = %s'
    cursor = connection.cursor()
    try:
        cursor.execute(Update, (new_food, game_id))
        connection.commit()
        print("Food level updated.")
    except Exception as e:
        print("Food update failed:", e)

    Check = 'SELECT food FROM game WHERE id = %s'
    try:
        cursor.execute(Check, (game_id,))
        result = cursor.fetchone()
        if result:
            food_level = int(result[0])
            print(f"Current food level: {food_level}")
            return food_level
        else:
            print("No record found.")
            return None
    except Exception as e:
        print("Food check failed:", e)
        return None"""