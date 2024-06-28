#!/usr/bin/python3

"""
This script uses a REST API to fetch and display
TODOS list progress for all employees,
and exports the data in JSON format.
"""

import json
import requests
import sys


def get_all_employees_todo_progress():
    """
    Fetches todos tasks for all employees.
    Exports the data to a JSON file.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch all employees data
    users_url = f'{base_url}/users'
    response_users = requests.get(users_url)

    if response_users.status_code != 200:
        print("Error fetching users data")
        return

    employees = response_users.json()

    # Initialize dictionary to hold all tasks
    all_tasks = {}

    for employee in employees:
        employee_id = employee.get('id')
        username = employee.get('username')

        # Fetch todos data for the current employee
        todos_url = f'{base_url}/todos?userId={employee_id}'
        response_todos = requests.get(todos_url)

        if response_todos.status_code != 200:
            print(f"Error fetching todo data for employee ID {employee_id}")
            return

        todos = response_todos.json()

        # Prepare tasks list for the current employee
        tasks = [{"username": username,
                  "task": task.get('title'),
                  "completed": task.get('completed')}
                 for task in todos]

        # Add tasks to the dictionary with employee ID as the key
        all_tasks[str(employee_id)] = tasks

    # Export tasks to JSON
    json_filename = "todo_all_employees.json"

    try:
        with open(json_filename, 'w') as file:
            json.dump(all_tasks, file, indent=4)
    except Exception as e:
        print(f"Error exporting data to {json_filename}: {e}")


if __name__ == '__main__':
    get_all_employees_todo_progress()
