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

    todo_list = requests.get(url_todo).json()
    name_response = requests.get(url_name).json()

    EMPLOYEE_NAME = name_response[0].get('name')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for i in todo_list:
        if i.get("completed"):
            NUMBER_OF_DONE_TASKS = NUMBER_OF_DONE_TASKS + 1
        TOTAL_NUMBER_OF_TASKS = TOTAL_NUMBER_OF_TASKS + 1

    print(
        "Employee {} is done with tasks({}/{}):".format(
            EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
        )
    )
    for complete in todo_list:
        if complete.get("completed"):
            print("\t {}".format(complete.get("title")))
