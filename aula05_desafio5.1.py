senha_correta="isabella"
idade=float(input("Informe a sua idade: "))
senha_correta=(input("Informe a sua senha: "))

if (senha_correta == "isabella") and (idade != 18):
    print("Acesso liberado! ")
else:
    print("Acesso negado! ")