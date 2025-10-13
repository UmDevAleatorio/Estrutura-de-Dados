#a) Índice-H com Busca Linear
def h_index_linear(citacoes):
    """
    Calcula o índice-h de um pesquisador usando busca linear.
    O array de citações deve estar ordenado em ordem decrescente.
    """
    h = 0
    #O número de artigos é o tamanho do array
    n = len(citacoes)
    for i in range(n):
        #Número de artigos até agora (i + 1)
        num_artigos = i + 1
        #Número de citações do artigo atual
        num_citacoes = citacoes[i]
        
        #O h-index é o máximo k tal que os k primeiros artigos têm pelo menos k citações
        #Como o array está em ordem decrescente, basta checar se o k-ésimo artigo tem
        #pelo menos k citações.
        if num_citacoes >= num_artigos:
            h = num_artigos
        else:
            #Como o array está ordenado, se a condição falhar aqui,
            #ela falhará para todos os próximos.
            break
    return h

#b) Índice-H com Busca Binária
def h_index_binaria(citacoes):
    """
    Calcula o índice-h de um pesquisador usando busca binária.
    O array de citações deve estar ordenado em ordem decrescente.
    """
    n = len(citacoes)
    inicio, fim = 0, n - 1
    h = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if citacoes[meio] >= meio + 1:
            #Esse é um possível índice-h. Tentamos encontrar um maior.
            h = meio + 1
            inicio = meio + 1
        else:
            fim = meio - 1
    return h

#Exemplo de Uso
citacoes_exemplo = [13, 8, 5, 4, 2, 1] # O h-index deve ser 4

#a) Executar a Busca Linear
h_linear = h_index_linear(citacoes_exemplo)
print("Índice-H com Busca Linear")
print(f"Citações: {citacoes_exemplo}")
print(f"O índice-h é: {h_linear}\n")

#b) Executar a Busca Binária
h_binario = h_index_binaria(citacoes_exemplo)
print("Índice-H com Busca Binária")
print(f"Citações: {citacoes_exemplo}")
print(f"O índice-h é: {h_binario}\n")

#Exemplo extra:
citacoes_exemplo_2 = [100, 50, 20, 10, 5] # O h-index deve ser 5
h_linear_2 = h_index_linear(citacoes_exemplo_2)
h_binario_2 = h_index_binaria(citacoes_exemplo_2)
print(f"Citações: {citacoes_exemplo_2}")
print(f"O índice-h (linear) é: {h_linear_2}")
print(f"O índice-h (binário) é: {h_binario_2}")