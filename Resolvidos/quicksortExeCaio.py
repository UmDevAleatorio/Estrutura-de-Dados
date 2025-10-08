def quicksort(arr):
    """
    Função principal que inicia o QuickSort.
    Não exige passar índices, apenas o array.
    """
    _quicksort(arr, 0, len(arr) - 1)  # Chama a função recursiva passando os índices corretos.

def _quicksort(arr, left, right):
    """
    Função recursiva que implementa o QuickSort.
    Divide o array em partes menores ao redor do pivô.
    """
    if left < right:  # Caso base: quando a subarray tem pelo menos 2 elementos.
        pi = partition(arr, left, right)  # Particiona o array e obtém o índice do pivô.
        
        # Chamada recursiva para a subarray à esquerda do pivô.
        _quicksort(arr, left, pi - 1)
        
        # Chamada recursiva para a subarray à direita do pivô.
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    """
    Função de particionamento: organiza o array para o QuickSort.
    Coloca o pivô em sua posição correta e garante:
        elementos <= pivô ficam à esquerda dele
        elementos > pivô ficam à direita dele
    """
    pivot = arr[right]  # Escolhe o último elemento como pivô.
    
    i = left - 1  # Ponteiro para a posição de troca: começa antes da subarray.

    # Percorre todos os elementos do subarray.
    for j in range(left, right):
        # Se o elemento atual for menor ou igual ao pivô...
        if arr[j] <= pivot:
            # Nessa parte eu fiz o avanço do ponteiro 'i' para indicar a próxima posição de troca.
            i += 1
            # Nessa parte eu fiz a troca entre o elemento atual (arr[j]) e o elemento na posição de troca (arr[i]).
            arr[i], arr[j] = arr[j], arr[i]
    
    # Após o loop, coloca o pivô na posição correta (entre os menores e os maiores).
    # Nessa parte eu fiz a troca final para colocar o pivô no seu lugar definitivo no array.
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    
    # Retorna o índice onde o pivô foi colocado.
    return i + 1


# Teste do algoritmo
nums = [2, 0, 3, 1, 1, 0]
quicksort(nums)
print(nums)