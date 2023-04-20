import requests

parameters = {
        "amount": 10,
        "type": "boolean",
        "category":27,
    }
response = requests.get("https://opentdb.com/api.php?amount=10&category=27&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]




