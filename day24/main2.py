with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# With "with" keyboards we don't need to put close()
with open("my_file.txt", mode="a") as file:
    file.write("New text.")

# Solo se puede un modo a la vez?

with open("../../Documents/GitHub/pythonBootCamp/day23/scoreboard.py") as prueba:
    prueba_python = prueba.read()
    print(prueba_python)
