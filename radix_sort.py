def base_radix(lista,exp):
    tamanho_lista = len(lista)
    output = [0] *tamanho_lista
    count = [0]*10

    for i in range(tamanho_lista):
        index = (lista[i] // exp ) % 10
        count[index] += 1

    for i in range(1,10):     
        count[i] += count[i-1]
    i = tamanho_lista - 1 
    while i >= 0:
        index = (lista[i] // exp) %10
        output[count[index]-1] = lista[i]
        count[index] -=1
        i-=1        
    
    for i in range(tamanho_lista): 
        lista[i] = output[i]

def radix_sort(lista):
    maximo = max(lista)
    exp = 1
    while maximo // exp > 0:
        base_radix(lista,exp)
        exp *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]        
radix_sort(arr)
print(arr)
        
