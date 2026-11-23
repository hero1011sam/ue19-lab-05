import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=10)
response.raise_for_status()
joke = response.json()

print(joke["setup"])
print(joke["punchline"])
