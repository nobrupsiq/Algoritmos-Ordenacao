def insertion_sort(lista):
    tamanho_da_lista = len(lista) # 5

    for i in range(1, tamanho_da_lista): 
        primeiro_elemento = i - 1
        segundo_elemento = lista[i]
        
        while primeiro_elemento >= 0 and lista[primeiro_elemento] > segundo_elemento: 
            lista[primeiro_elemento + 1] = lista[primeiro_elemento]
            primeiro_elemento -= 1

        lista[primeiro_elemento + 1] = segundo_elemento

    return lista


lista = [1, 9, 4, 5, 2, 3]
insertion_sort(lista)
print(lista)
