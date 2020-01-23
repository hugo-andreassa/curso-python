
entrada = [0, 0, 0, 0, 0, 0]
valores_positivos = 0

entrada[0] = float(input())
entrada[1] = float(input())
entrada[2] = float(input())
entrada[3] = float(input())
entrada[4] = float(input())
entrada[5] = float(input())

for i in entrada:
    if i >= 0:
        valores_positivos += 1

print("{} valores positivos".format(valores_positivos))
