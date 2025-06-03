def bucket_sort(lista):
    minimo = min(lista)
    maximo = max(lista)
    numero_baldes = len(lista)
    intervalo = (maximo - minimo+1) / numero_baldes
    baldes= []
    for _ in range(numero_baldes):
        baldes.append([])
    print(f'Intervalo por balde: ')
    print()

    for numero in lista:
        index = int((numero - minimo)/intervalo)
        if index == numero_baldes:
            index = numero_baldes -1
        baldes[index].append(numero)
        print(f'numero {numero} vai para o balde {index}')
        for i in range(numero_baldes):
            baldes[i] = sorted(baldes[i])
        resultado = []
        for balde in baldes:
            resultado.extend(balde)
        print(f'lista ordenada é {resultado}')    
            

arr = [10, 20, 5, 15,7,9,12,6, 25, 12, 18, 8]
bucket_sort(arr)