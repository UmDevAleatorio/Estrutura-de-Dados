from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()
    # Mapeamento de fechamentos para aberturas
    pares = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        # Se for abertura, empilha
        if char in "([{":
            pilha.push(char)
        # Se for fechamento, verifica se corresponde ao topo
        elif char in ")]}":
            if pilha.is_empty():
                return False  # Fechamento sem abertura
            topo = pilha.pop()
            if pares[char] != topo:
                return False  # Abertura e fechamento não correspondem

    # Se a pilha ficou vazia, está balanceado
    return pilha.is_empty()


# Testes
print(is_balanced("[{}(2+2)]{}"))    # Esperado True
print(is_balanced("[{}(2+2))]{}"))   # Esperado False
print(is_balanced("[{}])"))          # Esperado False
print(is_balanced("[()]{}{()()}"))   # Esperado True
print(is_balanced("[(])"))           # Esperado False
