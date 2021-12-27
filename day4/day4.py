#Randomisation and Python List
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

