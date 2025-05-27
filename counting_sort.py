#EXPLICAÇÂO
'''Primeiro usamos o array A para contar quantas vezes cada valor aparece, criando o array C.
Entao basicamente o C que fizemos primeiramente será todo alterado nessa nova fase a seguir.
Depois, fazemos a soma acumulativa de C, Fazemos isso somando cada posição com a anterior.

Por fim, percorremos A de trás pra frente e usamos C para montar o array B, que é o resultado ordenado.
exemplo para a criação do array B: iremos pegar o valor do A que esta sendo percorrido de tras pra frente, ir na posição dele no array C ( num - 1 para indice), e o valor do C servira de posição para colocarmos no array B, após isso subtrair 1 do valor do array C
no exemplo de antes, A = 3, fomos no C, vimos o numero da posição 3 (indice 2) que seria 5 e colocamos o 3 na quinta posição do array B, após isso o 5 vira 4 no array C.
'''


def counting_sort_verbose(A):
    print("Array A original:", A)

    k = max(A)          # Encontra o maior valor em A para definir o tamanho do array C
    n = len(A)          # Tamanho do array original A

    C = [0] * k         # Array de contagem (C), do tamanho do maior valor (índices de 0 até k-1)
    B = [0] * n         # Array de saída (B), onde os elementos ordenados serão armazenados

    # ===============================
    # Etapa 1: Contagem das ocorrências
    # ===============================
    print("\nPasso 1: Contagem dos elementos no array C")
    for num in A:
        C[num - 1] += 1   # Subtrai 1 para alinhar o valor ao índice (ex: valor 3 vai para índice 2)
        print(f"Contando {num}: C = {C}")

    # ===============================
    # Etapa 2: Soma acumulada (cumulativa)     
    # ===============================
    print("\nPasso 2: Cálculo acumulativo no array C")
    print('somando o valor com o numero anterior da lista')
    for i in range(1, k):
        C[i] += C[i - 1]  # Cada posição recebe a soma dela com a anterior
        print(f"Acumulando índice {i}: C = {C}")
    # Agora C[i] indica quantos elementos são menores ou iguais a (i + 1)

    # ===============================
    # Etapa 3: Construção do array B ordenado
    # ===============================
    print("\nPasso 3: Construção do array B ordenado (percorrendo A de trás para frente)")
    for i in reversed(range(n)):
        num = A[i]                 # Pega o valor atual de A
        pos = num - 1              # Calcula o índice correspondente em C
        B[C[pos] - 1] = num        # Usa o valor de C[pos] como posição em B (ajustado com -1)
        C[pos] -= 1                # Decrementa o valor em C, pois um elemento foi colocado
        print(f"Colocando {num} na posição {C[pos]} de B: B = {B}, C = {C}")

    print("\nArray B final ordenado:", B)
    return B

# Teste
A = [3, 2, 4, 7, 4, 7, 1, 2, 3]
counting_sort_verbose(A)
