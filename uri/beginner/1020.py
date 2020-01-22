
# Idade em dias

tempo = int(input())

ano = int(tempo/365)
tempo -= int(ano*365)

mes = int(tempo/30)
tempo -= int(mes*30)

dias = int(tempo/1)

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano, mes, dias))
