class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def get_height(node):
        if node is None:
            return 0
        return node.height

    def update_height(self):
        left_height = Node.get_height(self.left)
        right_height = Node.get_height(self.right)
        self.height = 1 + max(left_height, right_height)

    def get_balance_factor(self):
        return Node.get_height(self.left) - Node.get_height(self.right)

    def rotate_left(z):
        y = z.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.update_height()
        y.update_height()
        return y

    def rotate_right(z):
        y = z.left
        t3 = y.right
        y.right = z
        z.left = t3
        z.update_height()
        y.update_height()
        return y


class Arvore:
    def __init__(self):
        self.root = None

    def search(self, value):
        node = self.root
        if node is None:
            return False
        while node is not None:
            if value == node.value:
                print("found")
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            print(f"Nó {value} inserido")
            return

        path = [] 
        current = self.root
        parent = None
        while current is not None:
            parent = current
            path.append(current)
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return

        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        path.append(new_node)
        print(f"Nó {value} inserido")

        for i in range(len(path) - 1, -1, -1):
            node = path[i]
            node.update_height()
            balance = node.get_balance_factor()

            if balance > 1:
                if value < node.left.value:
                    new_subroot = Node.rotate_right(node)
                    print("rotate LL")
                else:
                    node.left = Node.rotate_left(node.left)
                    new_subroot = Node.rotate_right(node)
                    print("rotate LR")

            elif balance < -1:
                if value > node.right.value:
                    new_subroot = Node.rotate_left(node)
                    print("rotate RR")
                else:
                    node.right = Node.rotate_right(node.right)
                    new_subroot = Node.rotate_left(node)
                    print("rotate RL")
            else:
                new_subroot = node

            if i - 1 >= 0:
                parent_of_node = path[i - 1]
                if parent_of_node.left is node:
                    parent_of_node.left = new_subroot
                else:
                    parent_of_node.right = new_subroot
            else:
                # node was root
                self.root = new_subroot


arvore = Arvore()

values = [10, 5, 15, 3, 1, 20, 25, 18]

for v in values:
    arvore.insert(v)

arvore.search(20)
