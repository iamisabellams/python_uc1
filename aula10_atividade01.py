matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

matriz_4_4 = [
    [1, 11, 3, 41],
    [5, 23, 11, 8],
    [1, 2, 15, 4],
    [5, 19, 7, 8]
]

def matriz_1():
    print("Elemento (0,0):", matriz[0][0]) 
    print("Elemento (2,1):", matriz[2][1])

def imprimir_matriz():
    for linha in matriz:
        print(f"|", end=" ")
        for elemento in linha:
            print(elemento, end= ' | ')
        print()

def ler_matriz_certo():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor = int(input(f"Digite o valor para [{i}][{j}]: "))
            linha.append(valor)
            matriz.append(linha)
        for linha in matriz:
            print(linha)

def soma_matrizes():
    soma = 0
    for i in range(4):
        for j in range(4):
            soma=soma + matriz_4_4[i][j]
    print(f"Soma dos elementos é : {soma}")

def soma_matrizes2():
    soma = 0
    for i in range(4):
        soma=soma + sum(matriz_4_4[i])
    print(f"A soma é: {soma}")

def soma_matrizes3():
    soma = 0
    for linha in matriz_4_4:
        soma=soma + sum (linha)
    print(f"A soma é:  {soma}")

def valor_maior():
    for i in range(4):
        maior = matriz_4_4 [i] [0]
        for j in range (4):
            if matriz_4_4 [i][j] > maior:
                maior = matriz_4_4 [i][j]
        print(f"O maior valor da linha {i} é : {maior}")

def contagem_numeros_pares():
    vet_pares=[]
    vet_impares=[]
    pares = 0
    impares = 0
    for i in range(4):
        for j in range(4):
            if matriz_4_4[i][j] % 2 == 0:
                pares += 1
                vet_pares.append(matriz_4_4[i][j])
            else: 
                impares += 1
                vet_impares.append(matriz_4_4[i][j])

    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números impares: {impares}")
    print(f"Os números pares são: {vet_pares}!")
    print(f"Os números ímpares são: {vet_impares}!")

def multi_linhas():
    num = int(input("Digite um número para realizar a multiplicação : "))
    linha_escolhida = int(input("Digite a linha que deseja para ser multiplicada (0-3) : "))

    linha=matriz_4_4[linha_escolhida]
    
    for posicao in range(4):
        linha[posicao] = linha[posicao] * num

if __name__ == "__main__":

    # matriz_1()
    # imprimir_matriz()
    # ler_matriz_certo()
    # soma_matrizes()
    # soma_matrizes2()
    # soma_matrizes3()
    # valor_maior()
    # contagem_numeros_pares()
    multi_linhas()