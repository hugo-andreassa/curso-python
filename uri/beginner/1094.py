entrada = int(input())

sapos = 0
coelhos = 0
ratos = 0

for _ in range(0, entrada):
    cobaias = input().split()
    if cobaias[1] == "C":
        coelhos += int(cobaias[0])
    elif cobaias[1] == "R":
        ratos += int(cobaias[0])
    else:
        sapos += int(cobaias[0])

total = sapos + ratos + coelhos

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelhos))
print("Total de ratos: {}".format(ratos))
print("Total de sapos: {}".format(sapos))
print('Percentual de coelhos: %.2f' % float(((100 * coelhos) / total)), '%')
print('Percentual de ratos: %.2f' % float(((100 * ratos) / total)), '%')
print('Percentual de sapos: %.2f' % float(((100 * sapos) / total)), '%')
