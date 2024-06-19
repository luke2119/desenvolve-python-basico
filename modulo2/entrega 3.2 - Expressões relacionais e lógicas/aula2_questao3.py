# PRIMEIRO, COLETAMOS AS INFORMAÇÕES DO JOGADOR.
idade=int(input("Digite sua idade: "))
ndejogos=int(input("Quantos jogos diferentes de tabuleiro você já jogou? "))
jogosvencidos= int(input("Desses jogos, quantos já venceu? "))

# APLICAÇÃO DAS CONDICIONAIS
true16a18= idade >= 16 and idade <= 18
jogoumaisde3= ndejogos >= 3
venceumaisde1= jogosvencidos >= 1
aptoClube= true16a18 and jogoumaisde3 and venceumaisde1

# PRINT
print("Digite sua idade", (idade))
print("Já jogou pelo menos 3 jogos de tabuleiro?", (jogoumaisde3))
print("Quantos jogos já venceu?", (jogosvencidos))
print("Apto para ingressar no clube de jogos de tabuleiro:",(aptoClube))