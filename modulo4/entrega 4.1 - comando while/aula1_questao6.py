### PASSO 1- VARIÁVEIS INICIAIS
nCobaias=int(input("quantidade de experimentos registrados "))
totalCobaias=0
cobaiaS=0
cobaiaR=0
cobaiaC=0
contador=0    ### não esquecer

### PASSO 2 - CRIANDO A LÓGICA E ITERAÇÕES
while (contador < nCobaias):
    entrada= input("Informe o tipo de cobaia a ser registrada (Ex:para 10S para 10 Sapos): ")
    quantia= int(entrada[:-1])    # Convertendo para inteiro, removendo o último caractere (deixando assim apenas o número)
    tipo= entrada[-1]    # Obtendo o último caractere (deixando assim novamente '10S') como no exemplo.
    
    totalCobaias += quantia

    if(tipo=="S"):
        cobaiaS += quantia
    elif(tipo=="R"):
        cobaiaR += quantia
    elif(tipo=="C"):
        cobaiaC += quantia
    contador+=1 ### aumentando contador do loop (NÃO ESQUECER)
if(totalCobaias>0):
    percentualS=(cobaiaS/totalCobaias)*100
    percentualR=(cobaiaR/totalCobaias)*100
    percentualC=(cobaiaC/totalCobaias)*100
else:
    percentualS=0
    percentualR=0
    percentualC=0

### PASSO 3 - IMPRIMIR RESULTADOS DA LOGICA
print(f"Total: {totalCobaias} cobaias")
print(f"Total de coelhos: {cobaiaC}")
print(f"Total de ratos: {cobaiaR}")
print(f"Total de sapos: {cobaiaS}")
print(f"Percentual de coelhos: {percentualC: .2f}%")
print(f"Percentual de ratos: {percentualR: .2f}%")
print(f"Percentual de sapos: {percentualS: .2f}%")