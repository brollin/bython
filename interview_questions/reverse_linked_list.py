# Reverse a linked list.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def print_list(start):
    node = start
    while node:
        print node.data
        node = node.next

print 'creating linked list'

start = Node(0)
prev = start
for i in range(1,11):
    curr = Node(i)
    if prev:
        prev.next = curr
    prev = curr

print_list(start)

print 'reversing linked list'

prevNode = None
currNode = start
while currNode:
    nextNode = currNode.next
    currNode.next = prevNode
    prevNode = currNode
    currNode = nextNode
start = prevNode

print_list(start)

