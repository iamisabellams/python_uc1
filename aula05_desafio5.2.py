nota1=float(input("Digite a sua 1º nota: "))
nota2=float(input("Digite a sua 2º nota: "))

media=(nota1+nota2)/3

trabalho_extra=(input("Você fez trabalho extra <s/n> : "))
trabalho_extra=trabalho_extra.lower()

if media >=7 or trabalho_extra == "s":
    print("Você foi aprovado. Boas férias! ")
else:
    print("Você foi reprovado. ")