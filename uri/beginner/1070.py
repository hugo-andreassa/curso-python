entrada = int(input())

contador = 0

while contador < 6:
    entrada += 1
    if entrada % 2 != 0:
        print(entrada)
        contador += 1
