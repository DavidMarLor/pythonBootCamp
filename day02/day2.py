print("Este es el día 2")

#Exercise 1
#Write a program that adds the digits in a 2 digit number e.g. input 35 the output 3 +5 = 8
a = input("Introduce un numero: \n")
b = int(a[0])
c = int(a[1])
print("La suma de "+a+" es: ",(b+c))

#Exercise 2 
#Calculate BMI = w/h
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) **2
print(int(bmi))

#Exercise 3
#Life in week
#Create a program to tells you how many days, weeks and months we have left if
#we life until 90 years old.
#1 year = 365 days
#1 year = 52 weeks
#1 year = 12 months
age = int(input("What is your current age?\n"))
time_left = 90 - age
days = time_left * 365
weeks = time_left * 52
months = time_left *12
message = f"You have {days} days, {weeks} weeks, {months} and months left."
print(message)
print("You have "+str(days)+" days, "+str(weeks)+" weeks, "+str(months)+" and months left.")

#Final Exercise
#Tip Calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill\n"))
aux = bill + bill * (tip/100)
total = aux / people
print("Each person should pay:",total)