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
        i["task"] = i.pop("title")
        i["completed"] = i.pop("completed")
        name = users[0].get("name")
        i["username"] = name
        del i["userId"]
        del i["id"]
    data[sys.argv[1]] = todos

    with open(sys.argv[1] + ".json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1]
    )
    url_name = "https://jsonplaceholder.typicode.com/users?id={}".format(
        sys.argv[1]
    )
    todo_list = requests.get(url_todo).json()
    name_response = requests.get(url_name).json()

    make_json(name_response, todo_list)
