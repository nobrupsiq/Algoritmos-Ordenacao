def bubble_sort(lista):
  tamanho = len(lista)
  flag = True

  while flag:
    flag = False
    indice = 0

    while indice < tamanho -1:
      if lista[indice] > lista[indice + 1]:
        bau = lista[indice] # Com essa variável, eu não perco o meu primeiro indice da lista
        lista[indice] = lista[indice + 1]
        lista[indice + 1] = bau
        flag = True

      indice += 1
    tamanho -= 1
  return lista

lista = [4, 1, 9, 6, 5]
print(bubble_sort(lista))
# O bubble sorte, ele sempre vai subindo o maior numero para o final da lista, causando o efeito bolha(subindo)
# Porque em todo final de while eu decremento um numero da lista, pq eu sempre sei que o maior numero sempre vai esta no final da lista.