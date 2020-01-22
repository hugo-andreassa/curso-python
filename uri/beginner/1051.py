

# 0 - 400.00
# 400.01 - 800.00
# 800.01 - 1200.00
# 1200.01 - 2000.00
# Acima de 2000.00

entrada = float(input())
valor = 0.0

if 0 <= entrada <= 2000.00:
    print("Isento")
    exit()

elif 2000.01 <= entrada <= 3000.00:
    valor = (entrada * 0.08)

elif 3000.01 <= entrada <= 4500.00:
    valor = (entrada * 0.18)

elif entrada > 4500.00:
    valor = (entrada * 0.28)

print("R$ {0:1.2f}".format(valor))
