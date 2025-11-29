from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route("/prime_number/<int:number>", methods=["GET"])
def prime_number(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

airport_db = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "London Heathrow Airport", "Location": "London"},
    "KJFK": {"Name": "John F. Kennedy International Airport", "Location": "New York"},
    "EHAM": {"Name": "Amsterdam Schiphol Airport", "Location": "Amsterdam"},
}

@app.route("/airport/<icao>", methods=["GET"])
def airport_info(icao):
    """Returns airport name & location based on ICAO code."""
    icao = icao.upper()

    if icao in airport_db:
        response = {
            "ICAO": icao,
            "Name": airport_db[icao]["Name"],
            "Location": airport_db[icao]["Location"]
        }
    else:
        response = {"error": "Airport not found"}

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)

