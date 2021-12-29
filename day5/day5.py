"""
#Loops
fruits = ["apple", "pear", "peach"]

for fruit in fruits:
  print(fruit)

#for iterator in array:
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
aux = 0
for i in student_heights:
  aux = aux + i
  heights = aux/(len(student_heights))
print("El peso medio es: ",heights)
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
aux = student_scores[0]
for i in student_scores:
  if aux < i:
    aux = i
print(aux);
#for number in range (a,b):
#Write your code below this row 👇
aux = 0
for number in range(2,101,2):
  aux += number
print(aux)
#Write your code below this row 👇
for number in range(1,101):
  if number % 3 == 0:
    if number % 5 == 0:
      print("FizzBuzz")
    else:
      print("Fizz") 
  elif number % 5 == 0:
    if number % 3 == 0:
      print("FizzBuzz")
    else:
      print("Buzz")
  else:
    print(number)
"""
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Write your code below this row 👇
tamanio = nr_letters + nr_numbers + nr_symbols
password = [""]

random_int = random.randint(1,len(letters))
valor = random_int-1
password[0] = letters[valor]

for letter in range(1,nr_letters+1):
  random_int = random.randint(1,len(letters)) 
  valor=random_int-1
  aux = letters[valor]
  password.append(aux)

for number in range(1,nr_numbers+1):
  random_int = random.randint(1,len(numbers)) 
  valor=random_int-1
  aux = numbers[valor]
  password.append(aux)

for symbol in range(1,nr_symbols+1):
  random_int = random.randint(1,len(symbols)) 
  valor=random_int-1
  aux = symbols[valor]
  password.append(aux)

print(password)

contador = 0
for code in password:
  aux = code
  random_int = random.randint(1,len(password))
  valor = random_int - 1
  aux2 = password[valor]
  password[contador] = aux2
  password[valor] = aux
  contador += 1

print(password)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P