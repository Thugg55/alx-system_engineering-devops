#!/usr/bin/python3
""" Python script returns imformation about his/her TODO list
    progress using the REST API provided
"""
import requests
import sys
from sys import argv, exit

if __name__ == '__main__':
    if len(argv) != 2:
        exit(1)
    base_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    base_url2 = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    todo = requests.get(base_url).json()
    base_user = requests.get(base_url2).json()['name']
    done = [tk['title'] for tk in todo if tk['completed']]
    print(f"Employee {base_user} is done with tasks({len(done)}/{len(todo)}):")
    for title in done:
        print(f"\t {title}")
