class Node:
    def __int__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = None
    
    def get_height(self,node):
        if node is None:
            return 0
        return node.height
    def update_height(self,node):
        left_height = self.get_height(self.left)
        right_height = self.get_height(self.right)
        node.height = max(left_height,right_height)
    def get_balance_factor(self,node):
        if node is None:
            return 0
        return self.get_height(self.left) - self.get_height(self.right)
          

class Arvore:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        node = self.root

        while True:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    break
                else:
                    node = node.left

            elif value > node.value:
                if node.right is None:
                    node.right = Node(value)
                    break
                else:
                    node = node.right

            else:
                break

    def buscar(self, value):
        node = self.root

        if node is None:
            return False

        while node is not None:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False
