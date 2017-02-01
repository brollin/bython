# Implement BST and function find

class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def find(self, find_key):
        if self.key == find_key:
            return self.value
        if self.key > find_key:
            if self.left:
                return self.left.find(find_key)
            else:
                return None
        else:
            if self.right:
                return self.right.find(find_key)
            else:
                return None

    def __lt__(self, other):
        if other:
            return self.key < other.key
        
        raise TypeError()

    def __gt__(self, other):
        if other:
            return self.key > other.key
        
        raise TypeError()

    def __str__(self):
        return ", ".join([str(self.key), str(self.value)])

a = Node(1,'test')

print(a)

