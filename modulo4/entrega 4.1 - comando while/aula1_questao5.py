### PASSO 1 - PERGUNTE A QUANTIDADE DE PESSOAS
nPessoas=int(input("Qual a quantidade de pessoas? "))

### PASSO 2- IDENTIFICANDO SE É A QUANTIDADE DE PARTICIPANTES É VALIDA
if(nPessoas <= 0):
    print("O número de participantes não é válido.")
else:
    soma_idades=0
    contador=0

### PASSO 3 - UTILIZANDO WHILE PARA DIGITAR IDADES E SOMA-LAS
while (contador < nPessoas):
    idade=(int(input("Digite a idade do correspondente em questão: ")))
    soma_idades += idade
    contador += 1

if (nPessoas>0):
    media_idades= soma_idades/nPessoas
    print(f"A média da idade dos participantes é de:{media_idades: .2f} anos.")