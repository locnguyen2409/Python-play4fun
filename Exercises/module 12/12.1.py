import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Random Chuck Norris Joke:")
        print(data["value"])
    else:
        print("Error fetching joke")


get_chuck_norris_joke()
