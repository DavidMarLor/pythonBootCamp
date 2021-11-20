#Logical Operators and Control Flow
#if condition:
# do this
#else:
#do this
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print("You can ride the rollercoaster")
else:
  print("Sorry, you have to grow taller before you ride.")

#Exercise 1
#Write a program that works out whether if a given number is an odd or even number
number = int(input("Which number do you want to check?\n"))
 
if (number % 2) == 0:
  print("Is a even number")
else:
  print("Is a odd number")

#Exercise 2
#Calculate BMI = w/h
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) **2
if bmi < 18.5:
  message1 = f"Your BMI is {bmi} and you are underweight"
  print(message1)
elif bmi > 18.5 and bmi < 25:
  message2 = f"Your BMI is {bmi} and you are normal weight"
  print(message2)
elif bmi > 25 and bmi < 30:
  message3 = f"Your BMI is {bmi} and you are overweight"
  print(message3)
elif bmi > 30 and bmi < 35:
  message4 = f"Your BMI is {bmi} and you are obese"
  print(message4)
else:
  message5 = f"Your BMI is {bmi} and you are clinically obese"
  print(message5)

#Exercise 2.1

#Write a program that works out whether if a given year is a leap year. Every year that is 
#evenly divisible by 4, except every year that is divisible by 100 unless the year is also 
#divisible by 400

year = int(input("Which year do you want to check?\n"))
messageY = f"The year {year} is a leap year"
messageN = f"The year {year} is not a leap year"
if (year % 4) == 0:
  if (year % 100) == 0:
    if (year % 400) == 0:
      print(messageY)
    else:
      print(messageN)
  else:
    print(messageY)
else:
  print(messageN)


#Exercise 3
#Small Pizza = $15
#Medium Pizza = $20
#Large Pizza = $25

#Pepperoni for small pizza = $2
#Pepperoni for medium/large pizza = $3

#Extra cheese for any pizza = $1


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
bill = 0

if size == 'S':
  bill += 15
  if add_pepperoni == 'Y':
    bill += 2
    if extra_cheese == 'Y':
      bill += 1
  else:
    if extra_cheese == 'Y':
      bill += 1
elif size == 'M':
  bill += 20
  if add_pepperoni == 'Y':
    bill += 3
    if extra_cheese == 'Y':
      bill += 1
  else:
    if extra_cheese == 'Y':
      bill += 1
else:
  bill += 25
  if add_pepperoni == 'Y':
    bill += 3
    if extra_cheese == 'Y':
      bill += 1
  else:
    if extra_cheese == 'Y':
      bill += 1

print("Your final bill is: ", bill)

#Exercise 3.1
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Cuantas veces se encuentra TRUE LOVE en los nombres.

aux = name1.lower() + name2.lower()

t = aux.count("t")
r = aux.count("r")
u = aux.count("u")
e = aux.count("e")
l = aux.count("l")
o = aux.count("o")
v = aux.count("v")
e = aux.count("e")

score = t + r + u + e + l + o + v + e

message1 = f"Your score is {score}, you go together like coke and mentos."
message2 = f"Your score is {score}, you are alright together."
message3 = f"Your score is {score}."

if score < 10 and score > 90:
  print(message1)
elif score > 40 and score < 50:
  print(message2)
else:
  print(message3)

#Exercise final

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.\n")
if direction.lower() == 'right':
  print("Game over")
elif direction.lower() == 'left':
  action = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
  if action.lower() == 'swim':
    print("Game over")
  elif action.lower() == 'wait':
    color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if color.lower() == 'red':
      print("Game over")
    elif color.lower() == 'blue':
      print("Game over")
    elif color.lower() == 'yellow':
      print("You win!")
    else:
      print("Game over")
  else:
    print("Game over")
else:
  print("Game over")