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

        ganador = "Empate"

    elif (e1 == "Tierra" and e2 == "Fuego") or \
         (e1 == "Fuego" and e2 == "Agua") or \
         (e1 == "Agua" and e2 == "Tierra"):

        ganador = "Jugador 1"

    else:

        ganador = "Jugador 2"

    print("Resultado:", ganador)

    return ganador                           # Devuelve el ganador.


def guardar_partida(e1, e2, ganador):        # Guarda la partida en un archivo.

    archivo = open("historial.txt", "a")     # Abre el archivo en modo agregar.

    archivo.write("Jugador 1: " + e1 + "\n")

    archivo.write("Jugador 2: " + e2 + "\n")

    archivo.write("Ganador: " + ganador + "\n")

    archivo.write("----------------------\n")

    archivo.close()                          # Cierra el archivo.


# ---------------- PROGRAMA PRINCIPAL ----------------

print("====== DUELO DE ELEMENTOS ======\n")

elemento1 = elegir_elemento("Jugador 1")

print()

elemento2 = elegir_elemento("Jugador 2")

print("\nJugador 1 eligió:", elemento1)

print("Jugador 2 eligió:", elemento2)

print()

ganador = verificar_ganador(elemento1, elemento2)

guardar_partida(elemento1, elemento2, ganador)

print("\nLa partida fue guardada en historial.txt")