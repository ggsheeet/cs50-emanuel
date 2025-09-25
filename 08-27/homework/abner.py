def printMenAndGetChoice():
    print("\nSeleccione la operación a realizar:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Cambiar un valor")
    print("6. Salir")
    print("7. Igual (=) y mostrar resultado")
    return int(input("Ingrese el número de la operación (1-7): "))

def ejecutar_eleccion(valores, operaciones):
    eleccion = printMenAndGetChoice()

    # User step-3
    if eleccion in [1, 2, 3, 4]:
        if eleccion == 1:
            operaciones.append("+")
        elif eleccion == 2:
            operaciones.append("-")
        elif eleccion == 3:
            operaciones.append("*")
        elif eleccion == 4:
            operaciones.append("/")
        # operaciones = [operacion1]
        
        valor = float(input("Ingrese el siguiente valor: "))
        valores.append(valor)
        ejecutar_eleccion(valores, operaciones)
        # valores = [valor1, valor2]

    # User step-3
    elif eleccion == 5:
        print("\nValores actuales:", valores)
        try:
            idx = int(input("¿Qué valor desea cambiar? (índice empezando en 1): ")) - 1
            # valores has 2 values
            # user said 2
            # idx = 1
            if 0 <= idx < len(valores):
                nuevo = float(input("Ingrese el nuevo valor: "))
                valores[idx] = nuevo
            else:
                print("Índice inválido.")
        except:
            print("Entrada inválida.")

    elif eleccion == 6:
        print("Saliendo de la calculadora. Gracias por usarla.")

    elif eleccion == 7:
        expresion = ""
        # Expression concatenation
        for i, val in enumerate(valores):
            expresion += str(val)
            if i < len(operaciones):
                expresion += operaciones[i]
        try:
            resultado = eval(expresion)
            print("\nOperación:", expresion)
            print("Resultado final:", resultado)
        except ZeroDivisionError:
            print("Error: División entre cero.")
        except:
            print("Error en la operación.")

        repetir = input("\n¿Quieres volver a usar la calculadora? (si/no): ").lower()
        if repetir == "si":
            calculadora_mejorada()
        print("¡Gracias por usar la calculadora mejorada! Luis eres el mejor")

    else:
        print("Error: Opción no válida. Intente de nuevo.")

def calculadora_mejorada(): 
    print("=== Bienvenido a la Calculadora Mejorada ===\n")
    
    valores = []
    operaciones = []

    # User step-1
    try:
        valor = float(input("Ingrese el primer valor: "))
    except:
        return print("Invalid input, use numbers only")
        
    valores.append(valor)
    # valores = [valor1]

    # User step-2
    ejecutar_eleccion(valores, operaciones)

calculadora_mejorada()
