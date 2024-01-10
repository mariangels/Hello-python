


# Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola")

hola = str("hola")
print_upper_texts(hola)


from datetime import datetime;

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)

timestamp = now.timestamp()
print(timestamp)
