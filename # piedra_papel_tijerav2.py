import random

opciones = ["piedra", "papel", "tijera"]

def pedir_jugada():
    jugada = input("Tu jugada (piedra/papel/tijera): ").strip().lower()
    while jugada not in opciones:
        print("Entrada inválida, intentá de nuevo.")
        jugada = input("Tu jugada (piedra/papel/tijera): ").strip().lower()
    return jugada

def jugar(rondas_totales=5):
    victorias_necesarias = (rondas_totales // 2) + 1
    puntos_usuario = 0
    puntos_pc = 0
    ronda = 1

    while puntos_usuario < victorias_necesarias and puntos_pc < victorias_necesarias and ronda <= rondas_totales:
        print(f"\nRonda {ronda} — Puntos: Tú {puntos_usuario} | PC {puntos_pc}")
        jugada_usuario = pedir_jugada()
        jugada_pc = random.choice(opciones)
        print(f"La computadora eligió: {jugada_pc}")

        if jugada_usuario == jugada_pc:
            print("Empate.")
        elif (jugada_usuario == "piedra" and jugada_pc == "tijera") or \
            (jugada_usuario == "papel" and jugada_pc == "piedra") or \
            (jugada_usuario == "tijera" and jugada_pc == "papel"):
            print("¡Ganaste la ronda!")
            puntos_usuario += 1
        else:
            print("Perdiste la ronda.")
            puntos_pc += 1

        ronda += 1

    print("\n=== Resultado final ===")
    print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

    if puntos_usuario > puntos_pc:
        print("¡Ganaste el juego! ")
    elif puntos_usuario < puntos_pc:
        print("La computadora ganó el juego.")
    else:
        print("Empate total.")


jugar(5)
