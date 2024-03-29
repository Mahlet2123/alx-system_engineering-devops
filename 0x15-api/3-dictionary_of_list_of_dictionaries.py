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
    data_list = []
    dict_ = {}
    for user in users:
        u = user.get("id")
        for i in todos:
            if u == i.get("userId"):
                name = user.get("username")
                data["username"] = name
                data["task"] = i["title"]
                data["completed"] = i["completed"]
                data_list.append(data)
                data = {}
        dict_[u] = data_list
        data_list = []

    with open("todo_all_employees.json", "w") as f:
        json.dump(dict_, f)


if __name__ == "__main__":
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    url_name = "https://jsonplaceholder.typicode.com/users"
    todo_list = requests.get(url_todo).json()
    name_response = requests.get(url_name).json()

    make_all(name_response, todo_list)
