
# VARIÁVEIS DO TERRENO
comprimento=15
largura=25
preco_m2= 2500

# FORMULAS DO PROGRAMA
area_m2= comprimento*largura
preco_total=preco_m2*area_m2

# RESULTADO FINAL
print(f"O terreno possui {area_m2}m2 e custa R${preco_total: ,.2f}")
