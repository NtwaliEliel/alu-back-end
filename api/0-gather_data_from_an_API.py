#!/usr/bin/python3

"""
this REST API,
for a given employee ID,
returns information about his/her todos list progress.
"""

import json
import requests


def get_employee_todo_progress(employee_id):
    """
   Defining get_employee_todo_progress function
   """

    # Replace 'YOUR_API_URL' with the actual API URL
    api_url = 'YOUR_API_URL/todos?userId=' + str(employee_id)

    response = requests.get(api_url)

    if response.status_code == 200:
        # Parse JSON response
        todos_data = json.loads(response.content)

        # Calculate completed tasks and total tasks
        completed_tasks = 0
        total_tasks = 0
        for todo in todos_data:
            if todo['completed']:
                completed_tasks += 1
            total_tasks += 1

        # Get employee name from the first todos item
        employee_name = todos_data[0]['title']

        # Print employee TODOS list progress
        print(f"Employee {employee_name} "
              f"is done with tasks({completed_tasks}/{total_tasks}):")
        for todo in todos_data:
            if todo['completed']:
                print(f"\t{todo['title']}")

    else:
        print(f"Error retrieving employee data: {response.status_code}")


if __name__ == '__main__':
    # Get employee ID from command line argument
    Employee_id = int(input("Enter employee ID: "))

    get_employee_todo_progress(Employee_id)
