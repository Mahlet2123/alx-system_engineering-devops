#!/usr/bin/python3
"""
for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    url_name = "https://jsonplaceholder.typicode.com/users?id={}".format(
        sys.argv[1])
    todo_response = requests.get(url_todo)
    name_response = requests.get(url_name).json()
    todo_list = todo_response.json()
    for i in name_response:
        EMPLOYEE_NAME = i.get('name').strip()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for i in todo_list:
        if i.get("completed"):
            NUMBER_OF_DONE_TASKS = NUMBER_OF_DONE_TASKS + 1
        TOTAL_NUMBER_OF_TASKS = TOTAL_NUMBER_OF_TASKS + 1
    print(
        "Employee {} is done with tasks({}/{})".format(
            EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
        )
    )
    for i in todo_list:
        title = i.get("title")
        print("\t{}".format(title))
