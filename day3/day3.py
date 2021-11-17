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