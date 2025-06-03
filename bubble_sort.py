def bubble_sort(lista):
  tamanho = len(lista)

  for _ in lista:
    for indice in range(tamanho -1):
      if lista[indice] > lista[indice + 1]:
        lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
        
  return lista

lista = [4, 1, 9, 6, 5]
print(bubble_sort(lista))