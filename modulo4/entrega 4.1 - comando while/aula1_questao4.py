### passo 1 - variável
n=int(input("Digite um número: "))
maior=0

### passo 2 - logica condidional if e while
while (n > 0):
    x=int(input("Digite X: "))
    if(x > maior):
        maior=x
    n=n-1
else:
    print(f"maior é igual a: {maior}")