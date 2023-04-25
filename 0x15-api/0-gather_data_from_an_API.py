#!/usr/bin/python3
"""
for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/posts/{}'.format(sys.argv[1])
    response = requests.get(url)
    res_json = response.json()
    #EMPLOYEE_NAME = 
    #NUMBER_OF_DONE_TASKS = 
    #TOTAL_NUMBER_OF_TASKS = 
    print(res_json)
    print(response)
