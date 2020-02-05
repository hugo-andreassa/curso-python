resultados = []

entrada = ["", "1"]

while entrada[0] != entrada[1]:
    entrada = input().split()

    x = int(entrada[0])
    y = int(entrada[1])

    if x > y:
        resultados.append("Decrescente")
    elif x < y:
        resultados.append("Crescente")

for word in resultados:
    print(word)
