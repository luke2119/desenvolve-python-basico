# 1- CRIAMOS AS 2 VARIAVÉIS PARA ARMAZENAR OS VALORES A SEREM COMPARADOS
valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o segundo valor: "))
resultado=(valor1 + valor2)

# 2- CRIANDO AS CONDICIONAIS PARA AFIRMAR SE O NÚMERO É PAR OU IMPAR.
if(resultado % 2==0):
    print("a soma dos valores é par.")
else:
    print("a soma dos valores é impar.")