
# Média 3

entrada = input().split()

n1 = float(entrada[0])
n2 = float(entrada[1])
n3 = float(entrada[2])
n4 = float(entrada[3])

# Pesos: 2, 3, 4 e 1
media = (n1*2) + (n2*3) + (n3*4) + (n4*1)
media /= 10

print("Media: {m:1.1f}".format(m=media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")

    exame = float(input())
    media = (media + exame)/2

    print("Nota do exame: {e:1.1f}".format(e=exame))
    if exame >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: {m:1.1f}".format(m=media))
