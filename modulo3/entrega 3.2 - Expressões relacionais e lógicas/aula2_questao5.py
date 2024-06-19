# COLETANDO INFORMAÇÕES
idade=int(input("Qual a sua idade? "))
genero=input("Qual o seu gênero?(M ou F) ")
tempoTrabalhado=int(input("Trabalha a quanto tempo de carteira assinada? "))

# CRIANDO VARIÁVEIS
aposentarM = genero == "M" and (idade >=65 or tempoTrabalhado >=30 or (idade >= 60 and tempoTrabalhado >=25))
aposentarF = genero == "F" and (idade>= 60 or tempoTrabalhado >=30 or (idade >=60 and tempoTrabalhado >= 25))

aposentar= aposentarM or aposentarF

# PRINT
print("Esta pesssoa pode se aposentar?", aposentar)
