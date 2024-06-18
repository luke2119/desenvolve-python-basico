
# VARIÁVEIS DO TERRENO
comprimento= int(input("Digite o comprimento: ")
largura= int(input("Digite a largura: ")
preco_m2= float(input("Valor do m2: ")

# FORMULAS DO PROGRAMA
area_m2= comprimento*largura
preco_total=preco_m2*area_m2

# RESULTADO FINAL
print(f"O terreno possui {area_m2}m2 e custa R${preco_total: ,.2f}")
