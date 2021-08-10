from node import Node
import math
from distributed_system.tasks import first_queue, second_queue, third_queue

# Branch algorithm execution class
class Worker:
    input_file = ''  # Input file name
    output_file = ''  # output file name
    n = 0  # The size of the data matrix n*n
    matrix = []  # Store data matrix Behavior of a single task Time required for each worker to complete
    max = 0  # Upper bound Find the approximate value through the greedy algorithm
    min = 0  # The lower bound is composed of the minimum value of each group
    pt_nodes = []  # Store scalable nodes
    pt_flag = 0  # Whether the marking queue is used to end the algorithm
    min_leaf_node = None  # node with the least consumption

#  Initialization parameters
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.read_data()
        self.n = len(self.matrix)
        self.get_low_limit()
        self.get_up_limit()

 # Read data from the file Initialize the data matrix
    def read_data(self):
        with open(self.input_file) as source:
            for line in source:
                data_cluster = line.split(',')
                temp = []
                for value in data_cluster:
                    temp.append(int(value))
                    self.matrix.append(temp)


    # Using first task queue, get the sum of the minimum value of the lower bound of the data 
    def get_low_limit(self):
        min_value = first_queue.apply_async((self.n, self.matrix))
        self.min += min_value

    # Using second queue, get the upper bound of data Greedy algorithm
    def get_up_limit(self):
        worker_mark = second_queue.apply_async((self.n))

    # Greedy algorithm to obtain approximate optimal solution
        for i in range(self.n):
            temp = self.matrix[i]
            min_value = 5000
            index = 0
            for k in range(int(math.sqrt(self.n))):
                if worker_mark[k] == 0 and min_value > temp[k]:
                    min_value = temp[k]
                    index = k

        worker_mark[index] = 1  # Mark whether the worker is assigned
        self.max += min_value  # Cumulative upper limit

# Branch and Bound Algorithm
    def branch_limit(self):
        if self.pt_flag == 0:  # Start from the first layer
            for i in range(int(math.sqrt(self.n))):
                time = self.matrix[0][i]

        if time <= self.max: # The upper limit is not reached, create a node and join the queue
            node = Node()
            node.deep = 0
            node.cost = time
            node.value = time
            node.worker = i
            self.pt_nodes.append(node)
            self.pt_flag = 1


        while self.pt_flag == 1: # Permanent loop When the queue is empty, it ends according to the conditional judgment
            if len(self.pt_nodes) == 0:
                break   

        temp = self.pt_nodes.pop(0) # First in, first out
        present_node = temp
        total_cost = temp.cost
        present_deep = temp.deep

        # Initialize the worker allocation flag
        third_queue.apply_async((self.n, temp))

        if present_deep + 1 == self.n: # The leaf node of the last row directly allocates the result
            if self.min_leaf_node is None:
                self.min_leaf_node = present_node

            else:
                if self.min_leaf_node.cost > present_node.cost:
                    self.min_leaf_node = present_node
                else:
                    children = self.matrix[present_deep + 1]

        # Check whether the child nodes of this node meet the requirements for entering the queue
            for k in range(self.n):
                if children[k] + total_cost <= self.max and worker_mark[k] == 0:
                    node = Node()
                    node.deep = present_deep + 1
                    node.cost = children[k] + total_cost
                    node.value = children[k]
                    node.worker = k
                    node.father = present_node
                    self.pt_nodes.append(node)

    # Output the result of algorithm execution
    def output(self):
        file = open(self.output_file, 'a')
        temp = self.min_leaf_node
        Print("Minimum cost is:", temp.cost)

        File.write('The minimum cost is:' + str(temp.cost) + '\n')

        Print(" "+str(temp.worker+1) + "worker completed the first"+ \
            str(temp.deep+1) + "part of job")

        File.write('th'+str(temp.worker+1) + 'workers completed the first'+str(temp.deep+1) + 'parts of work\n')

        while temp.father is not None:
            temp = temp.father

        print(" "+str(temp.worker+1) + "worker completed the first"+str(temp.deep+1) + "part of job")

        File.write('th' + str(temp.worker + 1) + 'worker completed the first' + str(temp.deep + 1) + 'part of assignment\n')
        Print('Algorithm execution result and write to file:', self.output_file)



input_file = 'input.dat'
output_file = 'output.dat'


# Initialize algorithm execution class
worker = Worker(input_file, output_file)

# Execute branch and bound algorithm
worker.branch_limit()

# Output result
worker.output()

