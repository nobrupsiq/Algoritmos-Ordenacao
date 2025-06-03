def merge_sort(lista):
    if len(lista) <= 1: 
        return lista
    

    div = len(lista) // 2   
    esquerda = lista[:div]  
    direita = lista[div:]  

    sorted_esquerda = merge_sort(esquerda) 
    sorted_direita = merge_sort(direita)   

    return merge(sorted_esquerda, sorted_direita) 

def merge(esquerd, direit):
    entrada = [] 
    i = j = 0  

    while i < len(esquerd) and j < len(direit):
        if esquerd[i] < direit[j]: 
            entrada.append(esquerd[i]) 
            i = i + 1 
        else:
            entrada.append(direit[j]) 
            j = j + 1 
    
    entrada.extend(esquerd[i:]) 
    entrada.extend(direit[j:])  

    return entrada 

lista = [9,4,8,1,3,2]
a = merge_sort(lista) 
print(a)   
