# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=26619

### Functions ###

# Definición

def my_function():
    print("Esto es una función")

# Función con parámetros de entrada/argumentos

def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)

# Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

# Función con parámetros de entrada/argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}")

# Función con parámetros de entrada/argumentos por defecto

def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

# Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

hola = str("hola")
print_upper_texts(hola)
