# Tkinter GUI and arguments
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

window.mainloop()

# args
# unlimited Arguments def add(n1, n2):
#                       return n1 + n2


def add(*args):  # Array de elementos de entrada
    for n in args:
        print(n)


add(1, 2, 3, 4)

def calculate(**kwargs):
    print(kwargs)  #Diccionario que representa las claves y valores.

calculate(add=3, multiply=5)
