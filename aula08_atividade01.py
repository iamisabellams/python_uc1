"""
atividade 01, exercicio 01
"""

def saudacao():
    print("Olá, seja bem-vindo(a) ao curso de Python!")

    return saudacao

"""
atividade 01, exercicio 02
somar dois números e retornar o resultado
"""

def soma(a, b):
    return a + b

def teste_soma():
    resultado = soma(5, 7)
    print("A soma é:", resultado)

"""
atividade 01, exercicio 04
calcular o fatorial de um numero inteiro nao negativo
"""

def fatorial(n):
    if n < 0:
        return "Número inválido para fatorial."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def teste_fatorial():
    numero=int(input("\n\n\tInforme o valor do número : "))
    resultado=fatorial(numero)
    print(f"\n\n\tFatorial de {numero} é igual à : {resultado}\n\n")

if __name__ == "__main__":
    teste_fatorial()