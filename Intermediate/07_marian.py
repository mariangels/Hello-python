
import re


my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"


# match: busca al comienzo de la linea

match = re.match("lección", my_string, re.I)
print(match)
if match is not None:
    start, end = match.span()
    print(my_string[start:end])
else:
    print("No encontrado match")


# search: busca sin más
    
search = re.search("lección", my_string, re.I)
print(search)
if search is not None:
    start, end = search.span()
    print(my_string[start:end])
else:
    print("No encontrado search")


# findall

findall = re.findall("lección", my_string, re.I)
print(findall)


# split

print(re.split(":", my_string))


# sub

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))


## Expresiones Regulares

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

## Carácteres numéricos
pattern = r"\d"
print(re.findall(pattern, my_string))


## Carácteres NO numéricos
pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.com"
print(re.match(pattern, email))
