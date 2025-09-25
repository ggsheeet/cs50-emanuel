def suma(x1, x2):
  print(int(x1) + int(x2))

def resta(x1, x2):
  print(int(x1) - int(x2))

def multi(x1, x2):
  print(int(x1) * int(x2))

def div(x1, x2):
  print(int(x1) / int(x2))

def calculadora():
  op = input("Selecciona la operación deseada: 1) Suma 2) Resta 3) Multiplicación 4) División\n")

  x1 = input("Inserta un número\n")
  x2 = input("Inserta un número\n")

  print("Resultado: ")

  if op == "1":
    suma(x1, x2)
  if op == "2":
    resta(x1, x2)
  if op == "3":
    multi(x1, x2)
  if op == "4":
    div(x1, x2)

  again = input("\nDesea realizar otra operación: 1) Sí 2) No\n")
  if again != "2":
    calculadora()

calculadora()
  