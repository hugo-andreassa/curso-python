
# Salário com Bônus

nome = input()
salario = float(input())
vendas = float(input())

total = vendas * 0.15
total += salario

print("TOTAL = R$ {t:1.2f}".format(t=total))
