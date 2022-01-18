#Como construir una clase propia en python

class User:
  def __init__(self):
    print("new user being created...")


  #pass #Con esta palabra clave podemos dejar un metodo o clase vacio

user_1 = User()#Esto llama a init y lo que tiene dentro

user_1.id = "001"
user_1.username = "david"

#En python no hace falta que los atributos esten indicados dentro de la clase, se pueden crear en cualquier momento para el objeto.

print(user_1.username)

user_2 = User()
user_2.id = "002"
user_2.username = "jack"

print(user_2.username)

class Car:
  #Siempre self tiene que estar en las variables ya que es el mismo objeto al que le asignamos los atributos que se le pasan al llamar.
  def __init__(self,seats):
    self.seats = seats

  def enter_race_mode(self):
    self.seats = 2
    #El metodo llama al objeto y modifica los atributos necesarios. Si se va a hacer uso del mismo objeto es necesario pasarlo como parametro.

my_car = Car(5)

print(my_car.seats)

my_car.enter_race_mode()

print(my_car.seats)



