"""
aula 08, desafio 08 pt1
calculadora simples
"""
import sys

def calculadora(n1, n2, operacao):
    print(f"{n1} {operacao} {n2}")
    if operacao =="+":
        resultado = n1 + n2
    elif operacao == "-":
        resultado = n1 - n2
    elif operacao == "*":
        resultado = n1 * n2
    elif operacao == "/":
        resultado = n1 / n2
        if n2 == 0:
            return ("Erro de divisão por zero")
        return n1 / n2
    else:
        return ("Operação invalida!")
    
    print(f"{n1} {operacao} {n2} = {resultado}")

if __name__ == "__main__":
    argumentos=sys.argv[1:]
    print(argumentos)

    numero1=float(argumentos[0])
    numero2=float(argumentos[1])
    operacao=(argumentos[2])

    calculadora(numero1, numero2, operacao)