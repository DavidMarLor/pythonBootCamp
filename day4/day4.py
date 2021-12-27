"""#Randomisation and Python List
import random
import my_module

random_integer = random.randint(1, 10)

print(random_integer)

print(my_module.pi)

random_float = random.random()

print(random_float)

#Ejercicio 1
#Heads or tails Cara o Cruz

import random

moneda = random.randint(1, 2)

if moneda % 2 == 0:
  print("Ha salido cruz")
else:
  print("Ha salido cara") 

#Listas
#Una lista es una estructura de datos que organiza los datos a traves de una
#sola variable por ejemplo:

fruits = ["pera", "manaza"]

print(fruits[0])
"""
#Exercise 2
# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print("La cuenta le toca pagar a " + names[random.randint(0,len(names)-1)])

