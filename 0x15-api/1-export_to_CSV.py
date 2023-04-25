#!/usr/bin/python3
"""
for a given employee ID, returns information
about his/her TODO list progress.
"""
import csv
import requests
import sys


def make_csv(users=None, todos=None):
    """Turns payloads into CSV format"""
    titles = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(sys.argv[1] + ".csv", "w") as f:
        write = csv.DictWriter(f, fieldnames=titles, quoting=csv.QUOTE_ALL)
        for i in todos:
            write.writerow({"USER_ID": i.get("userId"),
                            "USERNAME": users[0].get("username"),
                            "TASK_COMPLETED_STATUS": i.get("completed"),
                            "TASK_TITLE": i.get("title")})


if __name__ == "__main__":
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    url_name = "https://jsonplaceholder.typicode.com/users?id={}".format(
        sys.argv[1])
    todo_list = requests.get(url_todo).json
    name_response = requests.get(url_name).json()

    make_csv(name_response, todo_list)
