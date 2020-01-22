
# Teste de Seleção 1

# se B for maior do que C e se D
# for maior do que A, e a
# soma de C com D for maior que a soma de A e B
# e se C e D, ambos, forem positivos
# e se a variável A for par

entrada = input()
entrada = entrada.split()

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
d = int(entrada[3])

teste = False

if b > c and d > a:
    teste = True
else:
    print("Valores nao aceitos")
    exit()

if c + d > a + b:
    teste = True
else:
    print("Valores nao aceitos")
    exit()

if c > -1 and d > -1 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
    exit()

