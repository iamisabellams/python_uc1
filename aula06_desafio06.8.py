soma = 0

while True:
    numero=int(input("Digite um número: "))
    if numero < 0:
        print("Encerrado.")
        break

    soma+=numero

    print(f"O valor da soma dos resultados é: {soma}")