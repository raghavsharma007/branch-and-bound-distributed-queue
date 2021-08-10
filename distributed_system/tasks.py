from time import sleep
from celery import Celery as task_distributer
import math

# Creating a celery instance with redis as message broker.
app = task_distributer('b_and_b', broker='redis://redis:6379/2')

# New code below
app.conf.task_routes = {
    'distributed_system.tasks.first_queue': {'queue': 'first_queue'},
    'distributed_system.tasks.second_queue': {'queue': 'second_queue'},
    'distributed_system.tasks.third_queue': {'queue': 'third_queue'}
}

@app.task
def first_queue(size, matrix):
    min_value = 0
    for i in range(size):
        min_value += min(matrix)
    return min_value


@app.task
def second_queue(size):
    # Initialize the worker to use the mark
    worker_mark = []
    for i in range(size):
        worker_mark.append(0)
    return worker_mark

@app.task
def third_queue(size, temp):
    # Initialize the worker to use the mark
    worker_mark = []
    for i in range(size):
        worker_mark.append(0)
    return worker_mark

    # Check the assignment of tasks under this node
    worker_mark[temp.worker] = 1
    while temp.father is not None:
        temp = temp.father
        worker_mark[temp.worker] = 1