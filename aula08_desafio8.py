"""
Arquivo com os desafios 5,6,7,8,9 e 10 da aula 08
OBS: De todos, não consegui fazer apenas o número 7.
"""

"""
Desafio 05: retornar o maior numero da lista
"""

def maior_elemento(lista):
    return max(lista)

numeros = [10, 55, 3, 18, 20, 97]
maior = maior_elemento(numeros)

print(f"O maior elemento da lista é: {maior}")

"""
Desafio 06: calcular a média aritmética dos elementos de uma lista
"""

def media(lista):
    return sum(lista) / len(lista)

numeros = [2, 4, 6, 8, 10]
resultado = media(numeros)

print(f"A média dos números listados é: {resultado}")

"""
Desafio 08: contar o número de vogais em uma string 
"""

def contar_vogais(texto):
    vogais = "AEIOU".lower()
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador

print("Número de vogais em 'Isabella':", contar_vogais("Isabella"))

"""
Desafio 09: retornar uma lista com a tabuada de um número de 1 a 10 
"""

def tabuada(n):
    resultados = []
    for i in range(1, 11):
        resultados = resultados + [n * i]  
    return resultados

print(f"Os resultados da tabuada de 8 é:", tabuada(8))

"""
Desafio 10: ordenar uma lista de tuplas com base no segundo elemento de cada tupla 
"""

def ordenar_por_segundo(lista_tuplas):
    lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1])
    return lista_ordenada

tuplas_exemplo = [("a", 2), ("b", 1), ("c", 3),]
resultado = ordenar_por_segundo(tuplas_exemplo)

print("Lista ordenada pelo segundo elemento de cada tupla:")
print(resultado)


if __name__ == "__main__":
    ordenar_por_segundo