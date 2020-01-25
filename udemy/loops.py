my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ------------------------------------------------------
# Exemplo simples de For Loop
# for num in my_list:
#    print(num)

# ------------------------------------------------------
# Exemplo simples de For Loop com Controle de Fluxo
# for num in my_list:
#    if num % 2 == 0:
#        print(num)
#    else:
#        print(f"Odd Number: {num}")

# ------------------------------------------------------
list_sum = 0
# Exemplo da forma de controlar blocos em python com identação
# for num in my_list:
#    list_sum = num + list_sum

# print(list_sum)

# Uso do _ quando não se pretende usar a variável
# for _ in "Hello World":
#    print("Cool!")

# ------------------------------------------------------
# tuple package
# my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
# print(len(my_list))

# tuple unpacked
# Tambem é comum ver ser os parenteses: a, b
# for (a, b) in my_list:
#     print(a)
#     print(b)

# ------------------------------------------------------
# for loop with dics
d = {'k1': 1, 'k2': 2, 'k3': 3}

# Por padrão ele itera atraves das chaves, não dos items,
# para iterar atraves dos items: items() function
# for key, value in d.items():
#    print(value)


# WHILE LOOPS ------------------------------------------------------
# while some_boolean_condition:
#   do something
# else:
#   do something else

x = 50

while x < 5:
    print("The current value of x is {}".format(x))

    x += 1
else:
    print("X IS NOT LESS THAN 5")

# break: interrompe o looping
# continue: reinicia o looping
# pass: não faz nada
