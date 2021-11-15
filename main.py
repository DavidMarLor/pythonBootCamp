print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
print("\n")
#atajos
print("Hello World!\nHello World!")
print("\nHello"+" David\n")
#Ejercicio 2 Si hay que introducir dentro del print "" o '' usar el opuesto para el print
print('Day 1 - String Manipulation')
print('String Concatenation is done with the "+" sign')
print('e.g. print ("Hello " + "world")')
print('New lines can be created with a backslash and n.')
#Funcion Input:
#Diferentes formas de usar input
print("\nUsando print para preguntar")
print("What is your name?\n")
print("Usando input como entrada de datos")
input("What is your name?\n")

#De esta forma primero se ejecuta el input y luego se incluye el nombre en el Hello
print("\nHello "+ input("What is your name?"))

#Ejercicio 3 Sacar el numero de caracteres de un nombre que se pregunta
print(len(input("What is your name? ")))

#Variables:
name = input("What is your name? ")
print("Valor de la variable name: " + name)

#Ejercicio 4: Intercambiar el valor de dos variables:
a = input("a: ")
b = input("b: ")
print("\nAntes de intercambiar")
print("a = "+ a)
print("b = "+ b)
print("\nDespues de intercambiar")
aux = a
a = b
b = aux
print("a = "+ a)
print("b = "+ b)