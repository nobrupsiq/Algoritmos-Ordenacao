def counting_sort(A):
    print("Array A original:", A)

    k = max(A)          
    n = len(A)          

    C = [0] * k         
    B = [0] * n         

    print("\nPasso 1: Contagem dos elementos no array C")
    for num in A:
        C[num - 1] += 1   
        print(f"Contando {num}: C = {C}")

    print("\nPasso 2: Cálculo acumulativo no array C")
    print('somando o valor com o numero anterior da lista')
    for i in range(1, k):
        C[i] += C[i - 1]  
        print(f"Acumulando índice {i}: C = {C}")
   
    print("\nPasso 3: Construção do array B ordenado (percorrendo A de trás para frente)")
    for i in reversed(range(n)):
        num = A[i]                 
        pos = num - 1              
        B[C[pos] - 1] = num        
        C[pos] -= 1               
        print(f"Colocando {num} na posição {C[pos]} de B: B = {B}, C = {C}")

    print("\nArray B final ordenado:", B)
    return B

# Teste
A = [3, 2, 4, 7, 4, 7, 1, 2, 3]
counting_sort(A)
