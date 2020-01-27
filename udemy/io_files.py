
# Aula de I/O em arquivos de texto

my_file = open('myfile.txt')

# A função .read() é usada para ler o arquivo
# uma unica vez pois o cursor estara no final
# do arquivo se usada de novo e o retorno sera ''
conteudo = my_file.read()

# Para resetar o lugar do ponteiro se usa a .seek(0)
my_file.seek(0)

# Retorno uma lista contendo as linhas do arquivo
linhas = my_file.readlines()

# O arquivo precisa sempre ser fechado para evitar
# de acontecer erros
my_file.close()

print(conteudo)
print(linhas)

# Para evitar precisar 'fechar' o arquivo ele pode ser
# inicializado dessa maneira (equivalente ao using do C#)
with open('myfile.txt') as my_new_file:
    print(my_new_file.read())

# Mudando o modo de abertura do arquivo
# r = read only
# w = write only (overwrite files or create new)
# a = append only
# r+ = reading and writing
# w+ = writing and reading (overwrite files or create new)
with open('myfile.txt', mode='a') as f:
    f.write('\nTeste de escrita.')

with open('myfile.txt') as f:
    print(f.read())






