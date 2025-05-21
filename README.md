
# Trabalho de implementação dos algoritmos de ordenação




## Algoritmos 💻

- Selection Sort (ordenação por seleção)
- Bubble Sort
- Insertion Sort (ordenação por inserção)
- Merge Sort (ordenação por intercalação)
- Quick Sort (ordenação rápida)
- Heap Sort
- Counting Sort
- Radix Sort
- Bucket Sort

## Aprendizados 📚


## 1. Selection Sort (Ordenação por seleção)
- O algoritmo percorre a lista várias vezes, a cada passada selecionando o menor (ou maior) elemento e colocando-o na posição correta.

- Mostra a importância de identificar mínimos/máximos e fazer trocas controladas.

- Utilizamos dois laços for aninhados, onde um percorre a lista e o outro busca o menor elemento no restante da lista.

- O Selection Sort sempre faz o mesmo número de comparações, independente da entrada:
``O(n²)`` no pior, médio e melhor caso.
Isso é útil para começar a entender análise de complexidade.

Demonstração 
![App Screenshot](./.github/img/selectionSort.gif)

## 2. Bubble Sort

- O Bubble Sort percorre a lista várias vezes, comparando elementos adjacentes e trocando-os de posição se estiverem fora de ordem.
- Isso nos ensina a detectar e corrigir posições erradas passo a passo.

- O nome "bubble" vem da ideia de que os maiores elementos "sobem" para o final da lista (como bolhas de ar na água).

- Podemos introduzir uma otimização que interrompe o algoritmo caso nenhuma troca seja feita em uma passada, mostrando a ideia de verificação de estado para melhorar desempenho.

- Mesmo com a otimização, a complexidade no pior caso ainda é ``O(n²)``.

- Melhor caso (lista já ordenada): ``O(n)`` com a otimização.

- Isso introduz a ideia de casos melhores e piores de desempenho.

Demonstração
![App Screenshot](./.github/img/bubble_sort.gif)