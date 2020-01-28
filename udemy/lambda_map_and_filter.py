# map() function
def square(num):
    return num ** 2


# a função map executa a função passada como parâmetro
# na lista passada como parâmetro
# print(list(map(square, [1, 2, 4, 5, 6])))


def slicer(text):
    if len(text) % 2 == 0:
        return "EVEN"
    else:
        return text[0]


# outro exemplo de uma função um pouco mais complexa
# print(list(map(slicer, ["Hugo", "And", "Paul", "Ericson"])))


# ------------------------------------------------------------
# filter() function
def check_even(num):
    return num % 2 == 0


# a função filter filtra a lista com base na função passada.
# a função passada obrigatoriamente deve retornar um booleano.
# print(list(filter(check_even, [1, 2, 3, 4, 5, 6])))


# ------------------------------------------------------------
# lambda function
def square(num):
    return num ** 2


#   |
#   |
#   |
#   \/

square = lambda num: num ** 2
# ainda pode ser usada como se fosse uma função
# print(square(10))

# forma mais comum de ser vista
lambda num: num ** 2

# lambda com map()
print(list(map(lambda num: num ** 2, [1, 2, 3, 4, 5, 6])))
print(list(map(lambda num: num[::-1], ["Hugo", "And", "Paul", "Ericson"])))

# lambda com filter()
print(list(filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5, 6])))
