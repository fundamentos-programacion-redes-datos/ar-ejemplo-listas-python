# Inicialización de variables
reporte_jugadores = "Listado de Jugadores\n"  # Cadena para almacenar la lista de jugadores
reporte_edades = "Listado de Edades\n"  # Cadena para almacenar las edades de los jugadores
suma_edades = 0  # Acumulador para calcular el promedio de edades
suma_estaturas = 0  # Acumulador para calcular el promedio de estaturas
contador = 0  # Contador para numeración de jugadores
bandera = True  # Variable de control para el ciclo while

# Uso de listas para almacenar datos de los jugadores y sus edades
lista_jugadores = []  # Lista para almacenar la información de los jugadores (nombre, posición, edad, estatura)
lista_edades = []  # Lista para almacenar solo las edades de los jugadores

# Bucle para ingreso de datos
while bandera:
    print("\nIngrese la información del jugador:")
    nombre = input("Nombre del jugador: ")  # Se solicita el nombre del jugador
    posicion = input("Posición en el campo de juego: ")  # Se solicita la posición del jugador
    edad = input("Edad del jugador: ")  # Se solicita la edad del jugador
    edad = int(edad)  # Conversión a entero
    estatura = input("Estatura del jugador (en metros): ")  # Se solicita la estatura del jugador
    estatura = float(estatura)  # Conversión a decimal

    # Uso de listas para almacenar la información de cada jugador
    contador = contador + 1  # Se incrementa el contador para numerar a los jugadores
    lista_jugador = [contador, nombre, posicion, edad, estatura]  # Se almacena la información en una lista
    lista_jugadores.append(lista_jugador)  # Se agrega la lista del jugador a la lista principal

    # Acumulación de sumas para calcular promedios
    suma_edades = suma_edades + edad  # Se acumulan las edades para calcular el promedio
    lista_edades.append(edad)  # Se almacena la edad en la lista de edades
    suma_estaturas = suma_estaturas + estatura  # Se acumulan las estaturas para calcular el promedio

    # Preguntar al usuario si desea continuar ingresando jugadores
    continuar = input("¿Desea ingresar otro jugador? (Sí/No): ")
    if continuar.lower() != "si":  # Si la respuesta no es "si", se termina el ciclo
        bandera = False

# Construcción del reporte de jugadores a partir de la lista de jugadores
for i in lista_jugadores:
    reporte_jugadores = f"{reporte_jugadores}{i[0]}. {i[1]} -{i[2]}-, edad {i[3]}, estatura {i[4]:.2f}\n"

# Construcción del reporte de edades a partir de la lista de edades
for i in lista_edades:
    reporte_edades = f"{reporte_edades}{i}\n"

# Cálculo de promedios de edad y estatura
if contador > 0:
    promedio_edades = suma_edades / contador  # Se calcula el promedio de edades
    promedio_estaturas = suma_estaturas / contador  # Se calcula el promedio de estaturas
else:
    promedio_edades = 0
    promedio_estaturas = 0

# Impresión del reporte final
print(reporte_jugadores)  # Se imprime el listado de jugadores
print(reporte_edades)  # Se imprime el listado de edades
print(f"Promedio de edades: {promedio_edades:.1f}")  # Se imprime el promedio de edades
print(f"Promedio de estaturas: {promedio_estaturas:.2f}")  # Se imprime el promedio de estaturas
