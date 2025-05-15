
def selectionSort(list):
    listaOrdenada = []
    while True:
        for item in list:
            if list[0] > list[0 + 1]:
                listaOrdenada.append(item)
            else:
                break

        return listaOrdenada


teste = [5,4,8,2,1,9]
resultado = selectionSort(teste)
print(resultado)
