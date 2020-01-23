
entrada = input().split()

comeco = int(entrada[0])
fim = int(entrada[1])

contador = 0
horas = comeco + 1

while horas != fim:
    horas += 1

    if horas == 24:
        horas = 0

    contador += 1

print("O JOGO DUROU {} HORA(S)".format(contador + 1))
