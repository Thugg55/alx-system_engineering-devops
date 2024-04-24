#!/usr/bin/python3
""" Python script returns imformation about his/her TODO list
    progress using the REST API provided
"""
import requests
import sys
from sys import argv, exit

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id)"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetching user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetching TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    print(f"\t{employee_name}: {completed_tasks}/{total_tasks}")

    # Display completed tasks
    print("Completed tasks:")
    for todo in todos_data:
        if todo['completed']:
            print(f"\t- {todo['title']}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)
    
    employee_id = int(argv[1])
    get_employee_todo_progress(employee_id)
