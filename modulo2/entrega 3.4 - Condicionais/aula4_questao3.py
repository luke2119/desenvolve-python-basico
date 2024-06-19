# PASSO 1 - CRIANDO AS CONDICIONAIS
ano=int(input("Digite o ano a ser verificado: "))

# PASSO 2 - CONSTRUINDO A LÓGICA DAS CONDICIONAIS ( PRIMEIRO, SE O ANO É DIVIDÍVEL POR 4 MAS NAO POR 100 E DEPOIS SE É DIVISÍVEL POR 400.)
if(ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
    print("Este ano é bissexto.")
else:
    print("Este ano não é bissexto.")