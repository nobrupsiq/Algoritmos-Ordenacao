def quick_sort(lista, inicio = 0, fim = None):
    if fim is None: 
        fim = len(lista) - 1
    if inicio < fim:
        pivo = particao(lista, inicio, fim)
        quick_sort(lista, inicio, pivo - 1)
        quick_sort(lista, pivo + 1, fim)


def particao(lista, inicio, fim):
    pivo_1 = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivo_1:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1

    lista[i], lista[fim] = lista[fim], lista[i]
    return i

lista = [9,8,7,1,6,2,5,3,4]
quick_sort(lista)
print(lista)
