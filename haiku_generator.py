import random

# Palabras organizadas por estaciones
invierno = {
    "elementos": ["nieve", "hielo", "lobo", "luna", "viento"],
    "adjetivos": ["frío", "blanco", "silencioso", "helado"],
    "acciones": ["cae", "brilla", "aúlla", "duerme"]
}

primavera = {
    "elementos": ["flor", "lluvia", "mariposa", "brote", "pájaro"],
    "adjetivos": ["suave", "fresco", "nuevo", "tierno"],
    "acciones": ["florece", "vuela", "canta", "crece"]
}

def elegir_estacion():
    print("¿Qué estación prefieres para tu haiku?")
    print("1. Invierno 🌨️")
    print("2. Primavera 🌸")
    opcion = input("Elige 1 o 2: ")
    return invierno if opcion == "1" else primavera

def crear_haiku(estacion):
    elemento = random.choice(estacion["elementos"])
    adjetivo = random.choice(estacion["adjetivos"])
    accion = random.choice(estacion["acciones"])
    
    haiku = f"""
✨ {elemento} {adjetivo}
   bajo el cielo infinito
   {accion} sin fin ✨
"""
    return haiku

# Crear y mostrar el haiku
estacion_elegida = elegir_estacion()
haiku = crear_haiku(estacion_elegida)
print("\n=================")
print(haiku)
print("=================")
