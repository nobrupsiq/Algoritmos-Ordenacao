def selectionSort(lista):
    for index in range(len(lista)):
        menor_index = index

        for j in range(index + 1, len(lista)):
            if lista[j] < lista[menor_index]:
                menor_index = j

        lista[index], lista[menor_index] = lista[menor_index], lista[index]
    return lista

lista = [4,1,6,2,7,9]

resultado = selectionSort(lista)
print(resultado)



