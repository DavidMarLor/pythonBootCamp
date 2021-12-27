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
#Exercise 2
# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print("La cuenta le toca pagar a " + names[random.randint(0,len(names)-1)])
"""

#Exercise 3
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal=position[0]
vertical=position[1]
if len(position) == 2:
  if vertical == "1":
    if horizontal == "1":
      row1[0] = 'X'
    elif horizontal == "2":
      row1[1] = 'X'
    elif horizontal == "3":
      row1[2] = 'X'
    else:
      print("Error no hay casillas para ese valor")
  elif vertical == "2":
    if horizontal == "1":
      row2[0] = 'X'
    elif horizontal == "2":
      row2[1] = 'X'
    elif horizontal == "3":
      row2[2] = 'X'
    else:
      print("Error no hay casillas para ese valor")
  elif vertical == "3":
    if horizontal == "1":
      row3[0] = 'X'
    elif horizontal == "2":
      row3[1] = 'X'
    elif horizontal == "3":
      row3[2] = 'X'
    else:
      print("Error no hay casillas para ese valor")
  else:
      print("Error no hay casillas para ese valor")
else:
  print("El valor introducido no tiene dos cifras")
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
