### passo 1 - variável
n1,n2,n3 =int(input("numero 1: ")),int(input("numero 2: ")),int(input("numero 3: "))
m=(n1+n2+n3)/3

### passo 2 - logica condidional if
if(m>= 60):
    print("Aprovado")
elif(m>= 40):
    print("Recuperação")
else:
    print("Reprovado")
print(round(m))
print("Fim.")