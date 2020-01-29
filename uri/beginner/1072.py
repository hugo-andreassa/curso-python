
entrada = int(input())
numeros = []

for x in range(0, entrada):
    numeros.append(int(input()))

result_in = [num for num in numeros if 10 <= num <= 20]
result_out = [num for num in numeros if num < 10 or num > 20]

print("{} in".format(len(result_in)))
print("{} out".format(len(result_out)))
