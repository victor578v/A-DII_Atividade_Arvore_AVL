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
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
            return

        no_atual = self.raiz

        while True:
            if valor < no_atual.valor:
                if no_atual.esquerda is None:
                    no_atual.esquerda = Node(valor)
                    break
                else:
                    no_atual = no_atual.esquerda

            elif valor > no_atual.valor:
                if no_atual.direita is None:
                    no_atual.direita = Node(valor)
                    break
                else:
                    no_atual = no_atual.direita

            else:
                break

    def buscar(self, valor):
        no_atual = self.raiz

        if no_atual is None:
            return False

        while no_atual is not None:
            if valor == no_atual.valor:
                return True
            elif valor < no_atual.valor:
                no_atual = no_atual.esquerda
            else:
                no_atual = no_atual.direita
        return False
