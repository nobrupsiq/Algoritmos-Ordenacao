def insertion_sort(lista):
    tamanho_da_lista = len(lista)

    for i in range(1, tamanho_da_lista): 
        chave = lista[i]
        primeiro_elemento = i - 1
        while primeiro_elemento >= 0 and lista[primeiro_elemento] > chave: 
            lista[primeiro_elemento + 1] = lista[primeiro_elemento]
            primeiro_elemento -= 1

        lista[primeiro_elemento + 1] = chave

    return lista


lista = [1, 9, 4, 5, 2, 3]
insertion_sort(lista)
print(lista)
