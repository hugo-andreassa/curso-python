

my_file = open('test.txt')

print(my_file.read())

# Para conseguir ler o 
# arquivo novamente é necessario 
# colocar o cursor na posição 0
my_file.seek(0)

with open('test.txt', mode='r+') as my_new_file:
	contents = my_new_file.readlines()


print(contents)

# Para não dar problema 
# ao outro programa 
# tentar acessar o arquivo 
my_file.close()


