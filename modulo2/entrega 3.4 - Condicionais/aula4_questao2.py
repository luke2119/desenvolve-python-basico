# PASSO 1 - CRIANDO AS VÁRIÁVEIS
avaliacao=int(input("O que você achou deste filme? (Dê a sua nota de 1 a 5): "))


# PASSO 2 - CRIAR A LOGICA UTILIZANDO CONDICIONAIS IF, ELIF E ELSE, DE MODO QUE 1-5 EQUIVALEM A NOTA ESPECIFICA DO ENUNCIADO E  QUALQUER OUTRA NUMERAÇÃO = INVALIDO.
if(avaliacao == 5):
    print("Excelente!")
elif(avaliacao == 4):
    print("Muito Bom!")
elif(avaliacao == 3):
    print("Bom.")
elif(avaliacao == 2):
    print("Regular.")
elif(avaliacao == 1):
    print("Ruim.")
else:
    print("Por favor, insira uma nota válida.")