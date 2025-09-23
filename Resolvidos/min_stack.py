from stack import Stack

class MinStack:
    """
    Pilha que permite, além das operações normais,
    consultar o menor valor em tempo O(1).
    """

    def __init__(self):
        self.main = Stack()   #Pilha principal
        self.min_aux = Stack()  #Pilha auxiliar para os mínimos

    def push(self, value):
        #Empilha um valor na pilha principal e atualiza a pilha auxiliar.
        self.main.push(value)

        #Se a pilha de mínimos está vazia ou o valor é menor/igual ao mínimo atual
        if self.min_aux.is_empty() or value <= self.min_aux.peek():
            self.min_aux.push(value)

    def pop(self):
        #Remove o elemento do topo da pilha principal.
        #Se esse elemento era o menor, atualiza a pilha auxiliar também.
        if self.main.is_empty():
            raise IndexError("Pilha vazia - não é possível desempilhar.")

        removed = self.main.pop()

        #Atualiza a pilha de mínimos se necessário
        if not self.min_aux.is_empty() and removed == self.min_aux.peek():
            self.min_aux.pop()

        return removed

    def peek(self):
        #Retorna o valor do topo da pilha principal sem removê-lo.
        return self.main.peek()

    def is_empty(self):
        #Verifica se a pilha principal está vazia.

        return self.main.is_empty()

    def size(self):
        #Retorna o tamanho da pilha principal.
        return self.main.size()

    def get_min(self):
        #Retorna o menor valor da pilha em tempo constante O(1).
        if self.min_aux.is_empty():
            raise IndexError("Pilha vazia - não existe mínimo.")
        return self.min_aux.peek()


# Testes
if __name__ == "__main__":
    pilha = MinStack()

    pilha.push(10)
    pilha.push(6)
    pilha.push(15)
    pilha.push(3)
    pilha.push(8)

    print("Mínimo atual:", pilha.get_min())  # Esperado 3

    pilha.pop()  # remove 8
    print("Mínimo atual:", pilha.get_min())  # Esperado 3

    pilha.pop()  # remove 3
    print("Mínimo atual:", pilha.get_min())  # Esperado 6

    pilha.push(2)
    pilha.push(4)
    print("Mínimo atual:", pilha.get_min())  # Esperado 2
