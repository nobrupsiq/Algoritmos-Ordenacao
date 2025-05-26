def merge_sort(lista):
    if len(lista) <= 1: # se a lista for menor ou igual a 1. Ela retorna ela mesma .
        return lista
    

    div = len(lista) // 2   # Aqui divide a lista em duas partes.
    esquerda = lista[:div]  # Metade da lista. Do inicio até antes do meio.
    direita = lista[div:]   # Outra metade da lista. Do meio até o final.

    sorted_esquerda = merge_sort(esquerda) # Ordena a parte da esquerda. Separada da direita.
    sorted_direita = merge_sort(direita)   # Ordena a parte da direita. Separada da esquerda.

    return merge(sorted_esquerda, sorted_direita) # Junta as duas listas. Na função marge.

def merge(esquerd, direit):
    entrada = [] # Lista vazia aonde vai receber os elementos já ordenados.
    i = j = 0    # São os indices atuas da esquerda e direita, começando em zero.

    while i < len(esquerd) and j < len(direit):
        if esquerd[i] < direit[j]: # Se o elemento da esquerda for menor.
            entrada.append(esquerd[i]) # Ele adiciona o elemento da esquerda.
            i = i + 1  # O indice i avança. do lado esquerdo.
        else:
            entrada.append(direit[j]) # Se o elemento da direita for menor ele e adicionado.
            j = j + 1 # O indice j avança. Do lado direito.
    
    entrada.extend(esquerd[i:]) # Se algum elemento do lado esquerdo tiver sobrado, ele adiciona no final da fila.
    entrada.extend(direit[j:])  # Se algum elemento do lado direito tiver sobrado, ele adiciona no final da fila.

    return entrada # Retorna a lista ordenada.


lista = [9,4,8,1,3,2]  # lista que vai ser ordenada.
a = merge_sort(lista)  # Chama a função merge_sort.
print(a)   # Exibe a lista ordenada.
