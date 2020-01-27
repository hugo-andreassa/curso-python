
def name_function():
    """
    DOCSTRING: information about the function.
    :return:
    """
    print("Hello World")


def dog_check(s):
    return 'dog' in s.lower()


# print(dog_check('My DOG is Boring'))

# PIG LATIN
def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word


# print(pig_latin('word'))
