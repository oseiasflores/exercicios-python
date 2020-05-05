metragem = float(input("Insira a metragem: "))
centimetos = metragem * 100

# Pra formatar float inserir %.{Numero de casas decimais}f e a variavel precisa ter % antes

print("%.2f" %metragem, "m equivale a %.2f" %centimetos, "cm")