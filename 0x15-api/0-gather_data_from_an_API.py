#!/usr/bin/python3
"""
for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    url_todo = url + "todos"
    url_name = url + "users/{}".format(sys.argv[1])

    params = {"userId": sys.argv[1]}

    todo_response = requests.get(url=url_todo, params=params).json()
    name_response = requests.get(url=url_name).json()

    completed = []
    for todo in todo_response:
        if todo.get("completed"):
            completed.append(todo.get("title"))
    print(
        "Employee {} is done with tasks({}/{}):".format(
            name_response.get("name"), len(completed), len(todo_response)
        )
    )
    for complete in completed:
        print("\t {}".format(complete))
