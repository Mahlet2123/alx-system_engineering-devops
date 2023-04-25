#!/usr/bin/python3
"""
for a given employee ID, returns information
about his/her TODO list progress.
"""
import json
import requests


def make_all(users=None, todos=None):
    """Turns payloads into JSON format"""
    data = {}
    for user in users:
        u = user.get("id")
        for i in todos:
            if u == i.get("userId"):
                name = user.get("username")
                i["username"] = name
                i["task"] = i.pop("title")
                i["completed"] = i.pop("completed")
                del i["userId"]
                del i["id"]
        data[u] = todos

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    url_name = "https://jsonplaceholder.typicode.com/users"
    todo_list = requests.get(url_todo).json()
    name_response = requests.get(url_name).json()

    make_all(name_response, todo_list)
