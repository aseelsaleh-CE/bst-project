class Node:
    def __init__(self, value):
        self.value = value 
        self.right = None
        self.left = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value:int):
        if self.root is  None:
            self.root = Node(value)
            return 
        
        current = self.root
        
        while current is not None:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return 
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return 
                current = current. right
            
        