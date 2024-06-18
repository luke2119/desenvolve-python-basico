juros=1.01
saldo=500.0

saldo=(saldo*juros) # primeiro mes
saldo=(saldo*juros) # segundo mes
saldo=(saldo*juros) # terceiro mes

print(f"O valor acumulado durante três meses é de: R${saldo}")