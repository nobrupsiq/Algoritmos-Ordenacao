
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
- Vantagens do Selection sort:
  - Número mínimo de trocas: Troca elementos apenas uma vez por iteração externa, o que pode ser útil quando o custo de troca é alto (ex: gravações em disco).
  - Fácil de entender e implementar: Ideal para quem está começando a estudar algoritmos de ordenação.
- Desvantagens:
  -Desempenho ruim para listas grandes: Possui complexidade O(n²) em todos os casos (melhor, médio e pior), o que o torna ineficiente para grandes conjuntos de dados.
  - Não é estável: Elementos iguais podem ter sua ordem alterada após a ordenação.
  



- ![App Screenshot](./.github/img/selectionSort.gif)

## 2. Bubble Sort

- O Bubble Sort percorre a lista várias vezes, comparando elementos adjacentes e trocando-os de posição se estiverem fora de ordem.
- Isso nos ensina a detectar e corrigir posições erradas passo a passo.

- O nome "bubble" vem da ideia de que os maiores elementos "sobem" para o final da lista (como bolhas de ar na água).

- Podemos introduzir uma otimização que interrompe o algoritmo caso nenhuma troca seja feita em uma passada, mostrando a ideia de verificação de estado para melhorar desempenho.

- Mesmo com a otimização, a complexidade no pior caso ainda é ``O(n²)``.

- Melhor caso (lista já ordenada): ``O(n)`` com a otimização.

- Isso introduz a ideia de casos melhores e piores de desempenho.
- Vantagens do bubble sort:
  - Simplicidade. É fácil de entender e implementar, o que o torna bom para fins educacionais.
  - Estável: Mantém a ordem de elementos iguais, o que é importante em algumas aplicações.
- Desvantagens:
  - Ineficiente para listas grandes: Possui complexidade de tempo O(n²) no pior caso e no caso médio, o que o torna impraticável para grandes conjuntos de dados.
  - Pouco usado na prática: Existem algoritmos muito mais eficientes como Quick Sort, Merge Sort ou até mesmo Insertion Sort.
  - Muitas trocas desnecessárias:
Troca elementos mesmo que eles estejam quase no lugar certo, desperdiçando tempo de execução.

- ![App Screenshot](./.github/img/bubble_sort.gif)

## 3. Insertion Sort

- A lógica do Insertion Sort é pegar um elemento e inseri-lo na posição correta dentro da parte da lista que já está ordenada.

- Assim como o Selection Sort, aprendemos a dividir a lista entre a parte ordenada e a não ordenada, mas aqui a inserção acontece de forma dinâmica, deslocando elementos conforme necessário.

- Ao inserir um novo elemento, outros precisam ser deslocados para a direita. Isso ensina como mover elementos dentro de uma estrutura como listas.

- Insertion Sort é mais rápido que Selection e Bubble Sort quando a lista está quase ordenada, com desempenho ``O(n)`` no melhor caso.
- Vantagens do Insertion Sort:
  - Fácil de implementar: É simples de entender e programar, ideal para fins educacionais.
  - Eficiente para listas pequenas ou quase ordenadas: Seu desempenho é bom quando a lista já está quase em ordem — pode atingir complexidade O(n) no melhor caso.
- Desvantagens:
  - Ineficiente para listas grandes: Possui complexidade O(n²) no caso médio e no pior caso, o que o torna ineficiente para grandes volumes de dados.
  - Mais lento que algoritmos avançados: É geralmente mais lento que algoritmos como Quick Sort, Merge Sort ou Heap Sort para listas grandes.


- ![App Screenshot](./.github/img/insertion_sort.gif)

## 4. Merge Sort

- O Merge Sort aplica a estratégia de "dividir para conquistar".

- Divide o problema em subproblemas menores (quebrando a lista ao meio), resolve os subproblemas (ordenando as metades), e combina (merge) os resultados em uma única lista ordenada.

- Merge Sort é naturalmente recursivo.

- Junta duas listas ordenadas em uma só.

- Merge Sort tem complexidade ``O(n log n)`` em todos os casos (melhor, médio e pior).
- Vantagens do Merge Sort:
  - Desempenho consistente: Possui complexidade de tempo O(n log n) em todos os casos (melhor, médio e pior), o que o torna muito eficiente para grandes volumes de dados.
  - Mantém a ordem dos elementos iguais, o que é útil em muitas aplicações.
- Desvantagens:
  - Mais lento em listas pequenas: Para conjuntos de dados pequenos, o Insertion Sort pode ser mais rápido devido ao overhead do Merge Sort.
  - Implementação mais complexa: É mais difícil de implementar corretamente que algoritmos simples como Bubble ou Insertion Sort.

- ![App Screenshot](./.github/img/merge_sort.gif)

## 5. Counting Sort

- Counting Sort é um algoritmo não-comparativo — ele conta quantas vezes cada valor aparece, em vez de comparar elementos.

- Isso mostra que nem toda ordenação precisa de ``if A > B`` para funcionar.

- O algoritmo só funciona bem quando sabemos o intervalo dos valores (por exemplo, de 0 a 100). Isso ensina que algoritmos podem ser super rápidos se usamos conhecimento extra sobre os dados. Exemplo: ordenar notas de alunos entre 0 e 10, ou idades entre 0 e 120.

- O Counting Sort usa um array auxiliar (vetor de contagem) para armazenar quantas vezes cada valor aparece.

- Quando os dados estão dentro de um intervalo pequeno, o Counting Sort tem complexidade ``O(n + k)``, onde:
  - ``n`` é o número de elementos,
  - ``k`` é o valor máximo (domínio dos dados).
- Vantagens do Couting Sort:
  - Altamente eficiente para intervalos pequenos de inteiros: Quando os valores estão dentro de um intervalo pequeno e conhecido, o Counting Sort pode ser mais rápido que algoritmos como Merge ou Quick Sort
  - Não usa comparações: Ao contrário de algoritmos como Bubble ou Merge Sort, ele não compara elementos diretamente, o que pode ser vantajoso em certas aplicações.
- Desvantagens:
  - Só funciona com inteiros (ou valores discretos): Não é aplicável a dados como números de ponto flutuante, strings longas, ou objetos complexos sem adaptação.
  - Se os números de entrada forem muito grandes ou dispersos, o array de contagem pode consumir muita memória, tornando o algoritmo ineficiente.

- ![App Screenshot](./.github/img/counting_sort.gif)


## 6. Quick sort

- Assim como o Merge Sort, o Quick Sort divide o problema em partes menores

- Escolhe um ``pivô`` Coloca os elementos menores à esquerda e maiores à direita (particiona) e aplica o mesmo processo recursivamente

- O algoritmo usa recursão para ordenar as sublistas criadas após a partição.

- Com isso aprendemos a importância da condição de parada e da chamada de função sobre subconjuntos

- A etapa de particionar a lista em torno de um pivô é o coração do Quick Sort

- Nos ensina a controlar índices (ex: dois ponteiros), fazer comparações e organizar os dados em tempo linear.

- A performance do Quick Sort depende da escolha do pivô

- Se for o pior possível (ex: sempre o maior ou menor), o algoritmo vira ``O(n²)``

- Com pivôs aleatórios ou do meio, atinge ``O(n log n)`` na média.
- Vantagens do Quick Sort:
  - Eficiente para grandes volumes de dados: É amplamente utilizado em bibliotecas padrão por seu desempenho consistente e rápido na média.
  - Apesar do pior caso ser O(n²), na média ele tem complexidade O(n log n) e é mais rápido que o Merge Sort na maioria dos casos, especialmente para arrays em memória
- Desvantagens:
  - Pior caso é O(n²): Se o pivô escolhido for sempre o menor ou maior elemento, o desempenho se degrada — embora isso possa ser evitado com técnicas como pivô aleatório ou mediana de três
  - Elementos iguais podem ter sua ordem relativa alterada durante a ordenação, o que pode ser problemático em certos contextos.

- ![App Screenshot](./.github/img/quick_sort.gif)
