frase="binding 13, keeping 13, saving 6, redeeming 6, taming 7"
palavras=frase.split()
contagem={}

for palavra in palavras:
    contagem[palavra]= contagem.get(palavra, 0) + 1

    print(contagem)