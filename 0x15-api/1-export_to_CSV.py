#!/usr/bin/python3
"""
python script export data in CSV format
"""
import csv
import requests
from sys import argv, exit


if __name__ == '__main__':
    if len(argv) != 2:
        exit(1)
    base_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    base_url_2 = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    tasks = requests.get(base_url).json()
    user = requests.get(base_url_2).json()
    with open(f"{argv[1]}.csv", 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow(
                [argv[1], user['username'], task['completed'], task['title']]
            )
