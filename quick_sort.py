def quick_sort(lista, inicio = 0, fim = None):
    if fim is None: 
        fim = len(lista) - 1 # Para ir para o índice do ultimo elemento.
    if inicio < fim: # Verifica se a lista tem mais de um elemento.
        pivo = particao(lista, inicio, fim) # chama a função particao para reorganizar a sublista entre inicio e fim em torno de um pivo. A função particao devolve o índice onde o pivô foi colocado corretamente.
        quick_sort(lista, inicio, pivo - 1) # Chama quick_sort recursivamente para ordenar a parte da lista antes do pivô.
        quick_sort(lista, pivo + 1, fim)    # Chama quick_sort para ordenar a parte da lista depois do pivô.


def particao(lista, inicio, fim):
    pivo_1 = lista[fim] # Escolhe o pivô como o último elemento da sublista.
    i = inicio # Cria um índice i que indica a posição onde os elementos menores ou iguais ao pivô serão colocados.
    for j in range(inicio, fim): # Laço que percorre a sublista do índice inicio até fim - 1.
        if lista[j] <= pivo_1:   # Se o elemento atual (lista[j]) for menor ou igual ao pivô.
            lista[j], lista[i] = lista[i], lista[j] # Troca o elemento lista[j] com lista[i].
            i = i + 1  # Avança o índice i para preparar a próxima posição onde um número menor ou igual ao pivô pode ser colocado.

    lista[i], lista[fim] = lista[fim], lista[i] # Depois do laço, coloca o pivô na posição correta: ele troca de lugar com lista[i].
    return i

lista = [9,8,7,1,6,2,5,3,4]
quick_sort(lista)
print(lista)
