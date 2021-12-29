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
"""
#for number in range (a,b):
#Write your code below this row 👇
aux = 0
for number in range(2,101,2):
  aux += number
print(aux)