from diccionarioMorse import dictMorse

frase = input("Introduce la frase a convertir: \n")
nueva_cadena = []

for letra in frase:
    if letra != ' ':
        nueva_cadena.append(dictMorse[letra.upper()])

print(nueva_cadena)
