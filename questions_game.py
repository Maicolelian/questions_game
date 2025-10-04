# Juego de preguntas con  puntuación

def obtener_color(puntos):
    if puntos == 2:
        return "🟧 Naranja"
    elif puntos == 4:
        return "🟨 Amarillo"
    elif puntos == 6:
        return "🟩 Verde claro"
    elif puntos == 8:
        return "🟩🟩 Verde oscuro"
    else:
        return "⚪ Blanco (sin aciertos)"

def juego_preguntas():
    print("🎮 Bienvenido al juego de preguntas por niveles")
    puntos = 0
    preguntas = [
        {"pregunta": "¿Cuánto es 3 + 5?", "respuesta": "8"},
        {"pregunta": "¿Cuál es el color del cielo en un día despejado?", "respuesta": "azul"},
        {"pregunta": "¿Qué número sigue después del 9?", "respuesta": "10"},
        {"pregunta": "¿Cuál es la capital de Colombia?", "respuesta": "bogota"}
    ]

    for i, p in enumerate(preguntas):
        print(f"\nPregunta {i+1}: {p['pregunta']}")
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == p["respuesta"]:
            puntos += 2
            print("✅ ¡Correcto! +2 puntos")
        else:
            print("❌ Incorrecto")

        print(f"Color actual: {obtener_color(puntos)}")
        print(f"Puntos acumulados: {puntos}")

    print("\n🏁 Fin del juego")
    print(f"🎯 Puntos totales: {puntos}")
    print(f"🎨 Color final: {obtener_color(puntos)}")

juego_preguntas()