entrada = input().split()

saida = [0, 0, 0]
saida[0] = float(entrada[0])
saida[1] = float(entrada[1])
saida[2] = float(entrada[2])

saida.sort(reverse=True)
a = saida[0]
b = saida[1]
c = saida[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a ** 2 > b ** 2 + c ** 2:
    print("TRIANGULO OBTUSANGULO")
elif a ** 2 < b ** 2 + c ** 2:
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or a == c:
    print("TRIANGULO ISOSCELES")