"""
Aula 09: Atividade 01
EX 01: Criando e imprimindo uma lista
"""

def criar_vetor_imprimir ():
    vetor=[1220, 21, 450, 40 ,5]
    print(f"\n\tOs valores do vetor é: {vetor}\n")

"""
Aula 09: Atividade 01
EX 02: Iterando sobre uma lista
"""

def iterar_imprimir_vetor ():
    vetor=[10, 21, 450, 40 ,5]
    for valor in vetor:
        print("\n\n Valores do vetor : {valor} \n")

"""
Aula 09: Atividade 01
EX 05: Calcular a soma dos elementos de um vetor
"""

def calcular_soma_vetores ():
    vetor = [2, 4, 6, 8, 10, 12]
    soma = sum(vetor)
    print(f"A soma dos elementos é : {soma}" )

"""
Aula 09: Atividade 01
EX 06: Encontrar o maior e o menor valor em um vetor
"""

def maior_menor():
    vetor = [4, 698, 10000, 4, 1]
    maior = max(vetor)
    menor = min(vetor)
    print(f"\n\n O maior número é : {maior} \n")
    print(f"\n\n O menor número é : {menor} \n")

"""
Aula 09: Atividade 01
EX 07: Inverter a ordem dos elementos de um vetor sem usar reverse()
"""

def inverter():
    vetor = [12, 14, 16 , 18, 20]
    vetor_invertido = vetor [:: -1]
    print(f"\n A lista com seus valores invertidos é : {vetor_invertido}\n")

"""
Aula 09: Atividade 01
EX 08: Multiplicar cada elemento do vetor por 2 e armazenar em um novo vetor
"""

def multiplicar_2():
    vetor = [2, 4, 6, 8, 10]
    multiplicador = 2
    vet_multiplicador = [elemento * multiplicador]
    for elemento in vetor:
        print (f"\n\n O valor da multiplicação é : {vet_multiplicador}\n")

"""
Aula 09: Atividade 01
EX 09: Contar quantas vezes o valor 3 aparece em um vetor
"""

def repetido():
    vetor = [3, 5, 7, 9, 4, 3, 3, 5, 1, 3, 10, 3]
    repeticoes = vetor.count(3)
    print(f"\n\n O número 3 aparece ... \n\n {repeticoes} vezes!\n\n")

"""
Aula 09: Atividade 01
EX 10: Ordenar um vetor em ordem crescente
"""

def ordenar():
    vetor = [5, 7, 9834, 2, 11, 4, 66]
    organizado = sorted(vetor)
    print(f"\n\n Abaixo segue os elementos do vetor organizados: \n\n {organizado} \n\n")

"""
Aula 09: Atividade 01
EX 11: Remover elementos duplicados do vetor
""" 

def remover():
    vetor = [1, 2, 2, 6 , 8 , 6 , 7, 8, 8, 9, 10, 3, 4, 4, 5]
    vetor_sem_duplicatas = list(dict.fromkeys(vetor) and sorted(vetor))
    print(f"\n\n Vetor sem duplicatas : {vetor_sem_duplicatas} \n\n ")

"""
Aula 09: Atividade 01
EX 11: Remover elementos duplicados do vetor
""" 

def separar_elementos():
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = [num for num in vetor 
        if num % 2 == 0]
    impar = [num for num in vetor 
        if num % 2 != 0]
    print(f"\n\n Os números pares são : {pares} \n\n")
    print(f"\n\n Os números ímpares são : {impar} \n\n")

"""
Aula 09: Atividade 01
EX 12: Calcular a média e exibir elementos acima da média
"""

def acima_media():
    vetor = [2, 4, 6, 8, 10]
    media = sum(vetor) / len(vetor)
    ac_media = [ num for num in vetor 
    if num > media]
    
    print (f"\n\n A média é : {media} \n\n E os números acima da média são : {ac_media}\n\n ")

if __name__ == "__main__" :

    # 01 criar e imprimir uma lista
    # criar_vetor_imprimir ()

    # 02 iterar e imprimir uma lista
    # iterar_imprimir_vetor ()

    # 05 calcular a soma dos elementos de um vetor
    # calcular_soma_vetores ()

    # 06 encontrar maior e menor em um vetor
    # maior_menor()

    # 07 inverter a ordem dos valores de uma lista
    # inverter()

    # 08 multiplicar cada elemento por 2 e armazenar um novo
    # multiplicar_2()

    # 09 repeticoes do numero 3
    # repetido()

    # 10 organizar os números do vetor
    # ordenar()

    # 11 Remover elementos duplicados do vetor
    # remover()

    # 12 Separar os elementos pares e ímpares em duas listas
    # separar_elementos()

    # 13 Calcular a média e exibir elementos acima da média
    # acima_media()