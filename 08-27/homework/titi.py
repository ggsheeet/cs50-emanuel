#TAREA CALCULADORA
#SUMA
def sumatiti():
    numero1 = input("Hora de sumar, primer número: ")
    numero2 = input("dame un numero: ")
    print(numero1)
    print(numero2)
    print(int(numero1)+int(numero2))
#REST
def restiti():
    numero1 = input("dame un numero: ")
    numero2 = input("dame un numero: ")
    print(numero1)
    print(numero2)
    print(int(numero1)-int(numero2))
#MULTI
def multiti():
    numero1 = input("dame un numero: ")
    numero2 = input("dame un numero: ")
    print(numero1)
    print(numero2)
    print(int(numero1)*int(numero2))
#DIVISION
def divititi():
    numero1 = input("dame un numero: ")
    numero2 = input("dame un numero: ")
    print(numero1)
    print(numero2)
    print(int(numero1)/int(numero2))

if (input("Deseas iniciar la calculadora? (si / no): ") == "si"):
    sumatiti()
    restiti()
    multiti()
    divititi()

#TAREA 2: LANZADOR
import random
def echar_suerte():
    return random.randint(800000, 100000000)

if (input("deseas sacar echar suertes? (si / no): ") == "si"):
   print("Has sacado un:", echar_suerte())

# Extra points
# Investigation
word_list = ["manzana", "platano", "cereza", "datil", "ciruela"]
random_word = random.choice(word_list)
print(f"Random Word: {random_word}")