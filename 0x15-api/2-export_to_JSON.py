#!/usr/bin/python3
"""
for a given employee ID, returns information
about his/her TODO list progress.
"""
import json
import requests
import sys


def make_json(users=None, todos=None):
    """Turns payloads into JSON format"""
    data = {}
    for i in todos:
        name = users[0].get("name")
        i["username"] =  name
    data[sys.argv[1]] = todos

    with open(sys.argv[1] + ".json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    url_name = "https://jsonplaceholder.typicode.com/users?id={}".format(
        sys.argv[1])
    todo_response = requests.get(url_todo)
    name_response = requests.get(url_name).json()
    todo_list = todo_response.json()
    EMPLOYEE_NAME = name_response[0].get('name')
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for i in todo_list:
        if i.get("completed"):
            NUMBER_OF_DONE_TASKS = NUMBER_OF_DONE_TASKS + 1
        TOTAL_NUMBER_OF_TASKS = TOTAL_NUMBER_OF_TASKS + 1
    make_json(name_response, todo_list)
