aluno = {}
    
aluno_1 = {"nome": "Johnny", "notas": [4, 8, 2]}
aluno_2 = {"nome": "Shannon", "notas": [3, 6, 10]}
aluno_3 = {"nome": "Joey", "notas": [2, 7, 5]}

print(f"Dados do aluno {aluno_1}")

print(f"As notas do aluno {aluno_1['nome']} são {aluno_1['notas']}")

media= sum (aluno_1['nome']) / len (aluno_1['notas'])
print(f" O aluno {aluno_1['nome']} obteve a media igual a : {media}")

aluno_1["media"]=media
print(f"Dados dos Aluno 1 {aluno_1}")