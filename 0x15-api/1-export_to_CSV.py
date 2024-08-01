#!/usr/bin/python3
""" 
    Python script uses an api https://jsonplaceholder.typicode.com
    to generate some fake data and some other fake stuudd:w
"""

import requests
from sys import argv

if __name__ == '__main__':
    todos = requests.get(f'https://jsonplaceholder.typicode.com/users/\
{argv[1]}/todos')

    employee_name = requests.get(f'https://jsonplaceholder.typicode.\
com/users/{argv[1]}').json()

    no_of_tasks = 0
    tasks_done = 0
    tasks_done_in = []
    a = todos.json()
    for i in a:
        if i.get('completed') is True:
            tasks_done += 1
            tasks_done_in.append(i.get('title'))
    for i in todos.json():
        no_of_tasks += 1

    with open(f"{argv[1]}.csv", mode='w', encoding='utf-8') as file:
        for task in todos.json():
            file.write(f'"{employee_name.get('id')}","{employee_name.get("username")}"\
,"{task.get("completed")}","{task.get("title")}"\n')
