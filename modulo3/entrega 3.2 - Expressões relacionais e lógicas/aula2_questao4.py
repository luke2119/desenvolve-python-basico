# COLETANDO INFORMAÇÕES (uso de strip e lower para evitar erros de digitação)
classe=input("Escolha a classe(guerreiro, mago ou arqueiro) ").strip().lower()
atrForca=int(input("Digite os pontos de força (de 1 a 20): "))
atrMagia=int(input("Digite os pontos de magia (de 1 a 20): "))

# CRIANDO CONDICIONAIS
classeValida = (classe == "guerreiro" and atrForca >= 15 and atrMagia <= 10) or \
    (classe == "mago" and atrForca <= 10 and atrMagia >= 15) or \
          (classe == "arqueiro" and 5 < atrForca <= 15 and 5 < atrMagia <= 15)

# PRINT
print("Pontos de atributo consistentes com a classe escolhida?",classeValida)
