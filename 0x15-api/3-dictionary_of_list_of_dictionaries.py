#!/usr/bin/python3
""" Script export data in JSON format """

import json
import requests


if __name__ == '__main__':
    base_url = f"https://jsonplaceholder.typicode.com/users/"
    users = requests.get(base_url).json()
    with open("todo_all_employees.json", "w") as f:
        json.dump({
           user['id']: [{
                "task": task['title'], "completed": task['completed'],
                "username": user['username']
                } for task in requests.get(f"{base_url}{user['id']}/todos")
                .json()]
           for user in users}, f)
