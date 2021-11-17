#Logical Operators and Control Flow
#if condition:
# do this
#else:
#do this
"""
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
"""
#Exercise 2.1
"""
Write a program that works out whether if a given year is a leap year. Every year that is 
evenly divisible by 4, except every year that is divisible by 100 unless the year is also 
divisible by 400
"""
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