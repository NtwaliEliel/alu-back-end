#!/usr/bin/python3
"""
This module fetches and displays
the TODOS list progress of an employee based on their ID.
It uses the 'requests' module to interact with a REST API
and the 'sys' module to handle
command-line arguments. Additionally, it exports the data in CSV format.
"""

import csv
import requests
import sys


def fetch_employee_data(emp_id):
    """
    Fetches employee data and todos tasks for a given employee ID.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch employee data
    user_url = f'{base_url}/users/{emp_id}'
    response_user = requests.get(user_url)

    if response_user.status_code != 200:
        print(f"Error fetching user data for employee ID {emp_id}")
        return None, None

    employee = response_user.json()
    employee_name = employee.get('name')

    # Fetch todos data
    todos_url = f'{base_url}/todos?userId={emp_id}'
    response_todos = requests.get(todos_url)

    if response_todos.status_code != 200:
        print(f"Error fetching todo data for employee ID {emp_id}")
        return None, None

    todos = response_todos.json()

    return employee_name, todos


def display_employee_todo_progress(employee_name, todos):
    """
    Displays the TODOS list progress of the employee.
    """
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} "
          f"is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


def export_tasks_to_csv(emp_id, employee_name, todos):
    """
    Exports the employee's tasks to a CSV file.
    """
    csv_filename = f"{emp_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow(
                [emp_id,
                 employee_name,
                 task.get('completed'),
                 task.get('title')])
    return "OK"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        Employee_Id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_Name, TODOS = fetch_employee_data(Employee_Id)

    if employee_Name and TODOS:
        result = export_tasks_to_csv(Employee_Id, employee_Name, TODOS)

        if result == "OK":
            sys.exit("Number of tasks in CSV: OK")
    else:
        print("Export failed.")
        sys.exit(1)  # Exit with status code 1 indicating failure
else:
    print("Failed to fetch employee data.")
    sys.exit(1)
