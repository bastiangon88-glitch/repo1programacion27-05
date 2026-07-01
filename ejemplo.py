elementos = ["Tierra", "Fuego", "Agua"]


def mostrar_elementos():                      # Muestra el menú de elementos.

    print("Elementos disponibles:")

    for i in range(len(elementos)):          # Recorre la lista.

        print(i + 1, "-", elementos[i])      # Muestra número y nombre.

    print()


def elegir_elemento(jugador):                # Permite elegir un elemento.

    print("Turno del", jugador)

    mostrar_elementos()

    opcion = int(input("Elige un elemento: "))

    return elementos[opcion - 1]             # Devuelve el elemento elegido.


def verificar_ganador(e1, e2):               # Compara los elementos.

    if e1 == e2:

        print("¡Empate!")

    elif (e1 == "Tierra" and e2 == "Fuego") or \
         (e1 == "Fuego" and e2 == "Agua") or \
         (e1 == "Agua" and e2 == "Tierra"):

        print("¡Gana el Jugador 1!")

    else:

        print("¡Gana el Jugador 2!")


# ---------------- PROGRAMA PRINCIPAL ----------------

print("====== DUELO DE ELEMENTOS ======\n")

elemento1 = elegir_elemento("Jugador 1")

print()

elemento2 = elegir_elemento("Jugador 2")

print("\nJugador 1 eligió:", elemento1)

print("Jugador 2 eligió:", elemento2)

print()

verificar_ganador(elemento1, elemento2)