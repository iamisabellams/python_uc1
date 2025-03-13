idade=float(input("Informe a sua idade: "))
habilitado=(input("Possui carteira de habilitação <s/n> : "))
habilitado=habilitado.lower()

if (idade >=18) and (habilitado == "s"):
    print("Você pode dirigir! ")
else:
    print("Você não pode dirigir! ")