class Node:
    def __init__(self):
        Self.deep = 0  # Mark the depth of the node
        Self.cost = 0  # Mark the total consumption to reach the node
        Self.father = None  # Mark the parent node of this node
        Self.value = 0  # The consumption value of this node
        Self.worker = None  # The task of this node is completed by the worker