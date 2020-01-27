entrada = [int(input()), int(input()), int(input()), int(input()), int(input())]

par = 0
impar = 0
positivo = 0
negativo = 0

for num in entrada:
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1

print("%d valor(es) par(es)\n%d valor(es) impar(es)\n%d valor(es) positivo(s)\n%d valor(es) negativo(s)" % (par, impar, positivo, negativo))

# print("{} valor(res) par(res)".format(par))
# print("{} valor(res) impar(res)".format(impar))
# print("{} valor(res) positivo(s)".format(positivo))
# print("{} valor(res) negativo(s)".format(negativo))
