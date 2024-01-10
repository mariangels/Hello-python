

 # Escribe un programa que muestre por consola (con un print) los
 # números de 1 a 100 (ambos incluidos y con un salto de línea entre
 # cada impresión), sustituyendo los siguientes:
 # - Múltiplos de 3 por la palabra "fizz".
 # - Múltiplos de 5 por la palabra "buzz".
 # - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


def fizzbuzz ():
    my_condition = 0
    while my_condition < 100:
        my_condition += 1
        if my_condition % 3 == 0 and my_condition % 5 == 0:
            print("fizzbuzz")
        elif my_condition % 3 == 0:
            print("fizz")
        elif my_condition % 5 == 0:
            print("buzz")
        else:
            print(my_condition)

def fizzbuzz_2 ():
    for index in range(0,101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)




def is_anagrama (texts, anagram_texts):

    if texts.lower() == anagram_texts.lower():
        return False
    if sorted(texts.lower()) == sorted(anagram_texts.lower()):
        return True
    else:
        return False
        
    

print(is_anagrama("prueba", "pruabe"))
print(is_anagrama("roma", "amor"))
