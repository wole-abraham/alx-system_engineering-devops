#!/usr/bin/python3
"""Python script uses an api https://jsonplaceholder.typicode.com"""

import json
import requests

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/users'
    dic = {}
    for info in requests.get(base_url).json():
        username = info.get('username')
        ids = info.get('id')
        url = base_url + "/" + str(ids) + "/todos"

        tasks = requests.get(url).json()
        for task in tasks:
            new_info = [{"username": username, "task": task.get('title'),
                         "completed": task.get('completed')} for task in tasks]
        dic[f"{ids}"] = new_info
    with open(f"todo_all_employees.json", mode='w', encoding='utf-8') as file:
        json.dump(dic, file)
