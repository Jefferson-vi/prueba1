import random

def obtener_opcion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(opcion_usuario, opcion_computadora):
    if opcion_usuario == opcion_computadora:
        return "Empate"
    elif (opcion_usuario == "piedra" and opcion_computadora == "tijera") or \
         (opcion_usuario == "tijera" and opcion_computadora == "papel") or \
         (opcion_usuario == "papel" and opcion_computadora == "piedra"):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

intentos = 10
for _ in range(intentos):
    print("Elige tu opción: piedra, papel o tijera")
    opcion_usuario = input().lower()

    if opcion_usuario not in ["piedra", "papel", "tijera"]:
        print("Opción inválida. Intenta de nuevo.")
        continue

    opcion_computadora = obtener_opcion_computadora()
    print("La computadora eligió:", opcion_computadora)

    resultado = determinar_ganador(opcion_usuario, opcion_computadora)
    print(resultado)
jugar()