# EXPLICAÇÃO

# 1 - Suponha que o primeiro elemento na matriz já esteja classificado.
# 2 - Percorra o array a partir do elemento na segunda posição e compare-o com o primeiro elemento já ordenado. Se o primeiro elemento for maior que o segundo, troque-os.
# 3 - Compare o terceiro elemento com os dois anteriores e, se for menor, troque novamente.
# 4 - Continue esse processo até que todo o array esteja classificado.

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n): # loop para percorrer a lista.
        chave = lista[i] # A chave recebe os objetos da lista.
        j = i - 1 # aqui o J recebe uma casa atras da chave.
        while j >= 0 and lista[j] > chave: 
            lista[j + 1] = lista[j] # Aqui o objeto J recebe uma casa afrente da que ele esta.
            j -= 1
        lista[j + 1] = chave # a chave vai receber uma casa a frente do objeto J.
    return lista
lista = [1, 9, 4, 5, 2, 3]
insertion_sort(lista)
print(lista)
