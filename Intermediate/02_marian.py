

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

# fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagrama (texts, anagram_texts):

    if texts.lower() == anagram_texts.lower():
        return False
    if sorted(texts.lower()) == sorted(anagram_texts.lower()):
        return True
    else:
        return False
        
    
# print(is_anagrama("prueba", "pruabe"))
# print(is_anagrama("roma", "amor"))


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    n = 0
    m = 1
    for index in range(0,51):
        variable = n + m
        print(variable)
        if index % 2 == 0: 
            m = variable
        else:
            n = variable

            
def fibonacci_2():
    n = 0
    m = 1
    for index in range(0,51):
        print(n)
        variable = n + m
        n = m
        m = variable

        
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
    
def is_primo(primo):
    if primo < 2:
        return False
    for index in range(2,primo-1):
        if primo % index == 0:
            return False
    print(primo)            
    return True
    

def primos():
    for index in range(0,101):
        is_primo(index)


# primos()
# print(is_primo(43))
        

#  Crea un programa que invierta el orden de una cadena de texto
#  sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
        
def invertir_cadena(cadena):
    print(cadena)
    reverse = ""
    index = len(cadena)
    while index >= 1:
        index -= 1
        reverse = reverse + cadena[index]
    print(reverse)

        
def invertir_cadena_2(cadena):
    print(cadena)
    reverse = ""
    lenght = len(cadena)
    for index in range(0,lenght):
        reverse += cadena[lenght-index-1]
    print(reverse)

invertir_cadena_2("Hola Mundo!")

