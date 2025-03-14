l1=float(input("Informe o primeiro lado do triangulo: "))
l2=float(input("Informe o segundo lado do triangulo: "))
l3=float(input("Informe o terceiro lado do triangulo: "))

if (l1 == l2 == l3):
    print("O seu triângulo é um Equilátero, possui lados iguais!! ")

elif (l1 == l2) or (l2 == l3) or (l3 == l1):
    print("O seu triângulo é um Isósceles, possui dois lados iguais!! ")

else:
    print("O seu triângulo é um Escaleno, possui todos os lados diferentes!! ")