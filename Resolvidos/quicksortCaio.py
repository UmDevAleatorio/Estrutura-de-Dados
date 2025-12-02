def quicksort(arr, inicio=0, fim=None):
    """
    Ordena um array utilizando o algoritmo Quicksort.
    """
    if fim is None:
        fim = len(arr) - 1
    if inicio < fim:
        pivo_indice = particionar(arr, inicio, fim)
        quicksort(arr, inicio, pivo_indice - 1)
        quicksort(arr, pivo_indice + 1, fim)
    return arr

def particionar(arr, inicio, fim):
    """
    Função auxiliar para o Quicksort que particiona o array.
    """
    pivo = arr[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

#a) Busca Linear para encontrar o alvo ou a posição de inserção
def busca_linear_insercao(arr, alvo):
    for i in range(len(arr)):
        if arr[i] == alvo:
            return i
        elif arr[i] > alvo:
            return i
    return len(arr)

#b) Busca Binária para encontrar o alvo ou a posição de inserção
def busca_binaria_insercao(arr, alvo):
    inicio, fim = 0, len(arr) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return inicio

#Exemplo de Uso
#Array desordenado de exemplo
arr_desordenado = [10, 80, 30, 90, 40, 50, 70]
alvo = 55

#1. Ordenar o array com Quicksort
arr_ordenado = quicksort(arr_desordenado.copy()) # Usamos uma cópia para manter o original
print(f"Array Original: {arr_desordenado}")
print(f"Array Ordenado: {arr_ordenado}")
print(f"Alvo: {alvo}\n")

#2a. Executar a Busca Linear
indice_linear = busca_linear_insercao(arr_ordenado, alvo)
print("Busca Linear")
print(f"O alvo {alvo} deveria ser inserido no índice: {indice_linear}\n")

#Exemplo com alvo que existe no array
alvo_existente = 70
indice_linear_existente = busca_linear_insercao(arr_ordenado, alvo_existente)
print(f"O alvo {alvo_existente} foi encontrado no índice: {indice_linear_existente}\n")

#2b. Executar a Busca Binária
indice_binario = busca_binaria_insercao(arr_ordenado, alvo)
print("Busca Binária")
print(f"O alvo {alvo} deveria ser inserido no índice: {indice_binario}\n")

#Exemplo com alvo que existe no array
indice_binario_existente = busca_binaria_insercao(arr_ordenado, alvo_existente)
print(f"O alvo {alvo_existente} foi encontrado no índice: {indice_binario_existente}\n")