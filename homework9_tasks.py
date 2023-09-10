import requests

url = 'https://dummyjson.com/todos'

params = {
    'limit': 150,
}

tasks = requests.get(url=url, params=params)

tasks_print = tasks.json()
todos = tasks_print['todos']

for todo in todos:
    if not todo['completed']:
        print(todo['todo'])
