#!/usr/bin/python3
"""Python script uses an api https://jsonplaceholder.typicode.com"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users'
    url = base_url + "/" + employee_id

    employee = requests.get(url)
    username = employee.json().get('username')

    todo_url = url + '/todos'
    tasks = requests.get(todo_url).json()

    with open(f"{argv[1]}.json", mode='w', encoding='utf-8') as file:

        info = [{"task": task.get('title'), "completed": task.get('completed'),
                 "username": username} for task in tasks]
        info = {employee_id: info}
        json.dump(info, file)
