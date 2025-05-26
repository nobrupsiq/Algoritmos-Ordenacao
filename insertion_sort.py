# EXPLICAÇÃO

# 1 - Suponha que o primeiro elemento na matriz já esteja classificado.
# 2 - Percorra o array a partir do elemento na segunda posição e compare-o com o primeiro elemento já ordenado. Se o primeiro elemento for maior que o segundo, troque-os.
# 3 - Compare o terceiro elemento com os dois anteriores e, se for menor, troque novamente.
# 4 - Continue esse processo até que todo o array esteja classificado.

def insertion_sort(lista):
  lenght_lista = len(lista) # Tamanho da lista

  for i in range(lenght_lista): # Looping do valor 0 até o tamanho da lista
    primeiro_elemento = lista[i] # Como diz a explicação o primeiro elemento precisa ja está classificado
    elemento_anterior = i -1 # Esse será o segundo elemento Exemplo: Se meu i é 3 o elemento_anterior será 2(Elemento atual e elemento anterior)

    while(elemento_anterior >= 0) and (primeiro_elemento < lista[elemento_anterior]):
      lista[elemento_anterior + 1] = lista[elemento_anterior]
      elemento_anterior -= 1
    lista[elemento_anterior + 1] = primeiro_elemento
  return lista

teste = [4,2,6,3,9,1]
print(insertion_sort(teste))