"""
#Loops
fruits = ["apple", "pear", "peach"]

for fruit in fruits:
  print(fruit)

#for iterator in array:
"""
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

