## PASSO 1 - CRIANDO AS VARIÁVEIS
peso_pacote=float(input("Digite o peso do pacote: "))
distancia_pacote=float(input("Digite a distancia do envio: "))
valor_frete=0

## PASSO 2 - CRIANDO A CONDICIONAL LÓGICA E PRINTANDO RESULTADO
if(distancia_pacote <= 100):
    valor_frete=(peso_pacote*1)
elif(101 >= distancia_pacote <= 300):
    valor_frete=(peso_pacote*1.5)
else:
    valor_frete=(peso_pacote*2)

## PASSO 3 - CONDICIONAL DA TAXA DE FRETE
if(peso_pacote > 10):
    valor_frete += 10

## PASSO 4 - IMPRIMINDO RESULTADO FINAL
print(f"O valor do frete é de R${valor_frete:,.2f}.")