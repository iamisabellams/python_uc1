idade=int(input("Informe a sua idade: "))
renda=float(input("Informe a sua renda mensal: "))
nome=input("Você tem nome sujo? <s/n> ")

if idade >= 21 and renda >= 2000 and nome=="n":
    print("Você pode realizar o empréstimo!! ")

else:
    print("Você não pode realizar o empréstimo")