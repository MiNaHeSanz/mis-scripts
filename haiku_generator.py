import random

# 1. Primero definimos el diccionario de estaciones (debe estar ANTES de las funciones)
estaciones = {
    'invierno': {
        'naturaleza': ['nieve', 'hielo', 'pino', 'montaña', 'lobo'],
        'acciones': ['tiembla', 'duerme', 'cubre', 'sopla', 'cae'],
        'elementos': ['frío', 'ventisca', 'escarcha', 'niebla', 'luna']
    },
    'primavera': {
        'naturaleza': ['flor', 'brote', 'nido', 'mariposa', 'jardín'],
        'acciones': ['brota', 'crece', 'florece', 'renace', 'vuela'],
        'elementos': ['lluvia', 'sol', 'brisa', 'rocío', 'pétalo']
    },
    'verano': {
        'naturaleza': ['playa', 'mar', 'palmera', 'cigarra', 'girasol'],
        'acciones': ['brilla', 'nada', 'canta', 'juega', 'descansa'],
        'elementos': ['ola', 'arena', 'calor', 'cielo', 'atardecer']
    },
    'otoño': {
        'naturaleza': ['hoja', 'castaña', 'seta', 'árbol', 'viento'],
        'acciones': ['cae', 'sopla', 'susurra', 'danza', 'vuela'],
        'elementos': ['niebla', 'lluvia', 'ocre', 'bosque', 'charco']
    }
}

def elegir_estacion():
    while True:
        print("¿Qué estación prefieres para tu haiku?")
        print("1. Invierno 🌨️")
        print("2. Primavera 🌸")
        print("3. Verano 🌞")
        print("4. Otoño 🍂")
        opcion = input("Elige 1-4: ")
        
        opciones = {
            "1": "invierno",
            "2": "primavera",
            "3": "verano",
            "4": "otoño"
        }
        
        if opcion in opciones:
            return opciones[opcion]
        else:
            print("❌ Por favor, elige una opción válida (1-4)")

def crear_haiku(nombre_estacion):
    # Accedemos al diccionario global estaciones usando el nombre_estacion como clave
    datos_estacion = estaciones[nombre_estacion]
    
    # Ahora seleccionamos elementos aleatorios de cada categoría
    naturaleza = random.choice(datos_estacion["naturaleza"])
    accion = random.choice(datos_estacion["acciones"])
    elemento = random.choice(datos_estacion["elementos"])
    
    # Creamos los versos
    verso1 = f"{naturaleza} {accion}"
    verso2 = f"{elemento} en el aire"
    verso3 = f"{naturaleza} {accion}"
    
    return f"{verso1}\n{verso2}\n{verso3}"

# Programa principal
if __name__ == "__main__":
    estacion_elegida = elegir_estacion()
    haiku = crear_haiku(estacion_elegida)
    print("\nTu haiku:\n")
    print(haiku)
    print("¡Espero que te haya gustado! 😊")