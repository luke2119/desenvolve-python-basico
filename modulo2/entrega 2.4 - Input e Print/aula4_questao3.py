# DADOS DO PRODUTO 1
nome_produto1= input("Digite o nome do produto 1: ")
preco_unit1= float(input("Digite o preço unitário deste produto: "))
quantidade1= int(input("Digite a quantidade de produtos: "))

# DADOS DO PRODUTO 2
nome_produto2= input("Digite o nome do produto 2: ")
preco_unit2= float(input("Digite o preço unitário deste produto "))
quantidade2= int(input("Digite a quantidade de produtos: "))

# DADOS DO PRODUTO 3
nome_produto3= input("Digite o nome do produto 3: ")
preco_unit3= float(input("Digite o preço unitário deste produto: "))
quantidade3= int(input("Digite a quantidade de produtos: "))

# SOMA DOS PRODUTOS
total=(preco_unit1*quantidade1)+(preco_unit2*quantidade2)+(preco_unit3*quantidade3)

print("Saída:")
print(f"Total: R${total: ,.2f}")