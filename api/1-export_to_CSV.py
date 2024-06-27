#!/usr/bin/python3

"""
this REST API,
for a given employee ID,
returns information about his/her todos list progress.
"""

import requests
import sys
import csv


def get_employee_todo_progress(emp_id):
    """
    Defining get_employee_todo_progress function
    """

    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee data
    user_url = f'{base_url}/users/{emp_id}'
    response_user = requests.get(user_url)

    if response_user.status_code != 200:
        print(f"Error fetching user data for employee ID {emp_id}")
        return

    employee = response_user.json()
    employee_name = employee.get('name')

    # Fetch todos data
    todos_url = f'{base_url}/todos?userId={emp_id}'
    response_todos = requests.get(todos_url)

    if response_todos.status_code != 200:
        print(f"Error fetching todo data for employee ID {emp_id}")
        return

    todos = response_todos.json()

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Display results
    print(f"Employee {employee_name} "
          f"is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    csv_filename = f"{emp_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ])
        for task in todos:
            writer.writerow([
                emp_id, employee_name, task.get('completed'), task.get('title')
            ])

    print(f"Data exported to {csv_filename}")


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
