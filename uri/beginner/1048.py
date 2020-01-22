
# 0 - 400.00
# 400.01 - 800.00
# 800.01 - 1200.00
# 1200.01 - 2000.00
# Acima de 2000.00

entrada = float(input())
salario = 0.0
porcentagem = 0.0
reajuste = 0.0

if 0 <= entrada <= 400.00:
    salario = (entrada * 0.15) + entrada
    porcentagem = "15 %"

elif 400.01 <= entrada <= 800.00:
    salario = (entrada * 0.12) + entrada
    porcentagem = "12 %"

elif 800.01 <= entrada <= 1200.00:
    salario = (entrada * 0.10) + entrada
    porcentagem = "10 %"

elif 1200.01 <= entrada <= 2000.00:
    salario = (entrada * 0.07) + entrada
    porcentagem = "7 %"

elif entrada > 2000.00:
    salario = (entrada * 0.04) + entrada
    porcentagem = "4 %"


reajuste = salario - entrada

print("Novo salario: {0:1.2f}".format(salario))
print("Reajuste ganho: {0:1.2f}".format(reajuste))
print("Em percentual: {}".format(porcentagem))
