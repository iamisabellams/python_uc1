"""
Aula 09 : Desafio 09 pt1
Soma de Elementos
"""

def soma_elementos():
    numeros = []
    for i in range(5):
        numero=int(input(f"Digite um números : "))
        numeros.append(numero)

    soma=sum(numeros)
    print(f"O resultado da soma é : {soma}")

"""
Aula 09 : Desafio 09 pt2
Números Ímpares de um Intervalo
"""
def impares_intervalo():
    for i in range(1, 51):
        if i %2 !=0:
            print(f"Este são os números ímpares entre 1 e 50 : ")
            
if __name__ == "__main__":
    
    # 01 soma elementos
    # soma_elementos()