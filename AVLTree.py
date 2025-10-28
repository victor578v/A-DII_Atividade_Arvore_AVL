class Node:
    def __int__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self):
        left_height = self.get_height(self.left)
        right_height = self.get_height(self.right)
        self.height = max(left_height, right_height)

    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(self.left) - self.get_height(self.right)

    def rotate_left(self, node):
        z = node
        y = node.right
        t2 = y.left
        y.left = z
        z.right = t2
        z.update_height(z)
        y.update_height(y)
        return y

    def rotate_right(self, node):
        z = node
        y = node.left
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
            return
        path = []
        current = self.root
        while True:
            path.append(current)
            if new_node.value < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            elif new_node.value > current.value:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
            else:
                return
            print(f"Nó {value} inserido")

        reversed = path[::-1]

        for item, index in reversed:  # index para encontrar o nó ancestral
            updated_height = item.update_height(item)
            balance_factor = item.get_balance_factor(item)

            if balance_factor > 1:
                if new_node.value < item.left:
                    item.rotate_left(item)
                else:
                    item.rotate_left(item.left)
                    item.rotate_right(item)
            if balance_factor < -1:
                if new_node.value > item.right:
                    item.rotate_left(item)
                else:
                    item.rotate_right(item.right)
                    item.rotate_left(item)


arvore = Arvore()

values = [10, 5, 15, 3, 1, 20, 25, 18]

arvore.insert(values)
