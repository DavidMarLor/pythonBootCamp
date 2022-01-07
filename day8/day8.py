#Funciones
def my_funcion():
  print("Esto es mi funcion")
my_funcion()

def greet():
  print("1")
  print("2")
  print("3")
greet()

name = input("What is your name?\n")
location = input("Where is your location?\n")

def greet_with_name(name,location):
  print(f"Hello {name}")
  print(f"How do you do {name}")
  print(f"What is it like in {location}")

greet_with_name(name,location)