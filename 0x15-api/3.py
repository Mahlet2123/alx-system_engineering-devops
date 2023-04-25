#!/usr/bin/python3
"""
for a given employee ID, returns information
about his/her TODO list progress.
"""
import json
import requests
import sys


def make_all(users=None, todos=None):
    """Turns payloads into JSON format"""
    all_list = []
    alljson = {}
    with open("todo_all_employees.json", "w") as f:
        for i in users:
            u = i.get("id")
            for i in todos:
                if u == i.get("userId"):
                    all_list.append({"username": users[0].get("username"),
                                     "task": i.get("title"),
                                     "completed": i.get("completed")})
            alljson[u] = all_list
        json.dump(alljson, f)

if __name__ == "__main__":
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    url_name = "https://jsonplaceholder.typicode.com/users"
    todo_response = requests.get(url_todo)
    name_response = requests.get(url_name).json()
    todo_list = todo_response.json()
    make_all(name_response, todo_list)
