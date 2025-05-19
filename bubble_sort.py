def bubble_sort(lista):
  tamanho = len(lista)
  flag = True
  storage = 0

  while flag:
    flag = False
    i = 0
    while i < tamanho -1:
      if lista[i] > lista[i + 1]:
        # Essa variavel storage armazena o meu primeiro indice, se não eu perco o indice e não consigo acesso
        storage = lista[i] # 4
        lista[i] = lista[i + 1]
        lista[i + 1] = storage
        flag = True
        i += 1
      tamanho -= 1
    return lista
  
lista = [4, 1, 6, 7, 9]
resultado = bubble_sort(lista)
print(resultado)