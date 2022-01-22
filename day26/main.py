# List and dictionaries
# List comprehesion saca una lista de una anterior

numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

new_list2 = [n+1 for n in numbers]

print(new_list)
print(new_list2)

name = "David"
letter_list = [letter for letter in name]
print(letter_list)

range_list = range(1, 5)
new_range = [n*2 for n in range_list]
# range_list = [num*2 for num in range(1, 5)] Mejor manera
print(new_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above

# Write your code below:
result = {word: len(word) for word in sentence.split()}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f = {day: weather_c[day] * 9/5 + 32 for day in weather_c}

print(weather_f)
