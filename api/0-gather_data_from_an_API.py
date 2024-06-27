#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee data
    user_url = f'{base_url}/users/{employee_id}'
    response_user = requests.get(user_url)

    if response_user.status_code != 200:
        print(f"Error fetching user data for employee ID {employee_id}")
        return

    employee = response_user.json()
    employee_name = employee.get('name')

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

    # Display results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_Id>')
        sys.exit(1)

    try:
        Employee_ID = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(Employee_ID)
