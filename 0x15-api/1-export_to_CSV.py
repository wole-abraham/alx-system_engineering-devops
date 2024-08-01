#!/usr/bin/python3
"""Python script uses an api https://jsonplaceholder.typicode.com"""

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


    with open(f"{argv[1]}.csv", mode='w', encoding='utf-8') as file:
        for task in tasks:
            file.write(f'"{employee_id}","{username}"\
,"{task.get("completed")}","{task.get("title")}"\n')
