def selectionSort(lista):
    # Lista
    for index in range(len(lista)):
        menor_index = index
        # Busca Menor Valor
        for indice_comparacao  in range(index + 1, len(lista)):
            if lista[indice_comparacao ] < lista[menor_index]:
                menor_index = indice_comparacao 

        lista[index], lista[menor_index] = lista[menor_index], lista[index]
    return lista

lista = [4,1,6,2,7,9]
resultado = selectionSort(lista)
print(resultado)



