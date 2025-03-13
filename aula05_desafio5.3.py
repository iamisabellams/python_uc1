idade=float(input("Qual a sua idade: "))

if idade < 18:
    pais=(input("Você está acompanhado dos pais <s/n> : ")).lower()
if pais == "s":
    print("Acesso Permitido. Boa festa!! ")
else:
    print("Acesso Negado. ")

if idade > 18:
    lista=input(int("Você está na lista de banidos <s/n> : ")).lower()

    if lista == "n":
        print("Acesso liberado. Boa festa!")