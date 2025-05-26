# EXPLICAÇÃO

# 1 - Suponha que o primeiro elemento na matriz já esteja classificado.
# 2 - Percorra o array a partir do elemento na segunda posição e compare-o com o primeiro elemento já ordenado. Se o primeiro elemento for maior que o segundo, troque-os.
# 3 - Compare o terceiro elemento com os dois anteriores e, se for menor, troque novamente.
# 4 - Continue esse processo até que todo o array esteja classificado.

def insertion_sort(lista):
    tamanho_da_lista = len(lista)

    for i in range(1, tamanho_da_lista): # loop para percorrer a lista.
        chave = lista[i] # A chave recebe os items da lista.
        primeiro_elemento = i - 1 # aqui o J recebe uma casa atras da chave.
        while primeiro_elemento >= 0 and lista[primeiro_elemento] > chave: 
            lista[primeiro_elemento + 1] = lista[primeiro_elemento] # Aqui o objeto primeiro_elemento recebe uma casa afrente da que ele esta.
            primeiro_elemento -= 1

        lista[primeiro_elemento + 1] = chave # a chave vai receber uma casa a frente do objeto primeiro_elemento.

    return lista


lista = [1, 9, 4, 5, 2, 3]
insertion_sort(lista)
print(lista)
