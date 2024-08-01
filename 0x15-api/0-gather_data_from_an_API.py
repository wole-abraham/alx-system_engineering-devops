#!/usr/bin/python3
""" Python script uses an api https://jsonplaceholder.typicode.com/
    to generate some fake data
"""

import requests
from sys import argv

if __name__ == '__main__':
    todos = requests.get(f'https://jsonplaceholder.typicode.com/users/\
{argv[1]}/todos')

    employee_name = requests.get(f'https://jsonplaceholder.typicode.\
com/users/{argv[1]}').json().get('name')

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

    print(f'Employee {employee_name} is done with tasks({tasks_done}\
/{no_of_tasks}):')
    for i in tasks_done_in:
        print(f'\t{i}')
