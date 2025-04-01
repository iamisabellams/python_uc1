pessoa={"nome": "Isabella", "idade": 20, "cidade": "Petrópolis"}
print(f"Dados da pessoa: {pessoa}")

pessoa["idade"]=19
print(f"Dados atualizados: {pessoa}")

pessoa["email"]="isabellamedeirosreal@gmail.com"
print(f"Dados atualizados:{pessoa}")

pessoa["sexo"]="f"

del pessoa["nome"]
del pessoa["email"]

print(f"Dados atualizados; {pessoa}")