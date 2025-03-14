nome=input("Digite o seu nome: ")
senha=input("Digite a sua senha: ")

if ( len(nome) < 3):
    print("Nome invalido!!!")

elif (len(senha) < 6):
    print("Senha invalida!!!")

elif (senha=="123456") or (senha=="senha"):
    print("Senha fraca. ")

else:
    print("Cadastro realizado com sucesso!!")