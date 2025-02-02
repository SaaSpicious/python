import requests

trivia_url = "https://opentdb.com/api.php?amount=10&type=boolean"
trivia_api = requests.get(url=trivia_url)

question_data = trivia_api.json()["results"]