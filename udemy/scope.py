# LEGB Rule
#
# L: Local - Nomes designados dentro de uma função(def, lambda),
# e não de forma global naquela função
#
# E: Enclosing function locals - Nomes declarados no escopo
# local de todas e qualquer função fechada(def, lambda), de dentro para fora
#
# G: Global(module) - Nomes designados no topo de um arquivo de modulo(module file),
# ou declarado globalmente em uma função(def) sem o arquivo
#
# B: Built-in - Nomes pré-designados na construção padrão do modulo do python
# (open(), range(), SyntaxError...)
#

# ---------------------------------------------------
# Exemplo - L
lambda num: num ** 2

# ---------------------------------------------------
# Exemplo - E

# GLOBAL
name = "This is a global string"


def greet():
    # ENCLOSING
    name = "Sammy"

    # Essa função está dentro do Escopo da função greet()
    # por isso ela consegue "enxergar" a variável name
    def hello():
        name = "I'am Local"
        # print("Hello " + name)

    hello()


greet()

# ---------------------------------------------------
# Exemplo - G
x = 50


def func():
    # busca a variável no escopo global
    global x
    print("x is {}".format(x))

    # faz uma mudança local
    # em uma variável global
    x = "NEW VALUE"
    print("I JUST LOCaLLY CHANGED GLOBAL X TO ".format(x))


func()
print(x)