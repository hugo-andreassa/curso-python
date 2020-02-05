entrada = int(input())

lista_resultados = []

for x in range(0, entrada):
    # primeiro valor tem peso 2, o segundo valor
    # tem peso 3 e o terceiro valor tem peso 5
    entrada = input().split()
    valor1 = float(entrada[0]) * 2
    valor2 = float(entrada[1]) * 3
    valor3 = float(entrada[2]) * 5

    resultado = (valor1 + valor2 + valor3) / 10

    lista_resultados.append(resultado)

for num in lista_resultados:
    print("{0:1.2}".format(num))
