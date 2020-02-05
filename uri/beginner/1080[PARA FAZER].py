from random import randrange
lista_entrada = []
maior = 0
index = 0

for x in range(1, 101):
    lista_entrada.append(int(input()))
    # lista_entrada.append(randrange(0, 1000))

for ind, num in enumerate(lista_entrada):
    if num >= maior:
        print(len(lista_entrada))
        maior = num
        index = ind

print(maior)
print(index)
