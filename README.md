Following files/directories are present in the directory:
input.dat: input for algorithm
node.py: class defining node of the tree
run.py: defining worker class, input, optimal solution using greedy and distributed queue and output
distributed_system:
task.py: defined tasks

Distributed task queues: 3 task queues are used
first_queue: to get the sum of the minimum value of the lower bound of the data.
second_queue: to get the upper bound of data Greedy algorithm.
third_queue: Initialize the worker allocation flag.

For starting distributed queues
$ celery -A distributed_system.tasks worker -l debug -Q first_queue
$ celery -A distributed_system.tasks worker -l debug -Q second_queue
$ celery -A distributed_system.tasks worker -l debug -Q third_queue

In-memory DB: Redis is used, port- 6379