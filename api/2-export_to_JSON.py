#!/usr/bin/python3

"""
This script uses a REST API to fetch
and display TODOS list progress for a given employee ID,
and exports the data in JSON format.
"""

import requests
import sys
import json


def get_employee_todo_progress(employee_id):
    """
    Fetches employee data and todos tasks for a given employee ID.
    Displays the TODOS list progress and exports the data to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
    """

    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee data
    user_url = f'{base_url}/users/{employee_id}'
    response_user = requests.get(user_url)

    if response_user.status_code != 200:
        print(f"Error fetching user data for employee ID {employee_id}")
        return

    employee = response_user.json()
    employee_name = employee.get('name')
    username = employee.get('username')

    # Fetch todos data
    todos_url = f'{base_url}/todos?userId={employee_id}'
    response_todos = requests.get(todos_url)

    if response_todos.status_code != 200:
        print(f"Error fetching todo data for employee ID {employee_id}")
        return

    todos = response_todos.json()

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Export tasks to JSON
    json_filename = f"{employee_id}.json"
    tasks = [{"task": task.get('title'), "completed": task.get('completed'), "username": username} for task in todos]
    data = {str(employee_id): tasks}

    try:
        with open(json_filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error exporting data to {json_filename}: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_Id>')
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
