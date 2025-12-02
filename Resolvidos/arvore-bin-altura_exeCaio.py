class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        node = Node(data)
        self.root = node

    # Percurso em ordem simétrica ("in-order")
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.simetric_traversal(node.left)
        print(node)
        if node.right:
            self.simetric_traversal(node.right)
    
    # Percurso em PÓS ORDEM em ÁRVORE BINÁRIA:
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)

        print(node)

    def height(self, node=None):
        if node is None:
            node = self.root

        if node is None:
            return -1

        left_h = self.height(node.left) if node.left else -1
        right_h = self.height(node.right) if node.right else -1

        return 1 + max(left_h, right_h)

        

def example_tree():
    tree = BinaryTree()
    n1 = Node('B')
    n2 = Node('A')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n6 = Node('F')


    n5.right = n6
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n2
    return tree
    
    


    #      'A'
    #    /     \
    #  'B'      'C'
    #          /   \
    #        'D'    'E'
    #                 \
    #                 'F' 


    # B A D C E F (Simetrico - InOrder)
    # B D F E C A (Pós Ordem - PostOrder)

    





if __name__ == '__main__':
    tree = example_tree()
    print("Simetrico - InOrder")
    tree.simetric_traversal() 
    
    tree2 = example_tree()
    print("")
    print("Pós Ordem - PostOrder")
    tree2.postorder_traversal() 


    # Altura da árvore inteira
    altura_total = tree.height()
    print(f"\nAltura da árvore inteira: {altura_total}")

    # Altura de um nó específico (exemplo: nó '-')
    no_E = tree.root.right.right #navegando na árvore.
    altura_E = tree.height(no_E)
    print(f"Altura a partir do nó '{no_E.data}': {altura_E}")