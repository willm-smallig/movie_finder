'''
Crear un programa en el que el usuario introduzca el título de una película.
El programa debe buscar la película en la lista peliculas.
Si la encuentra, debe mostrar el título, el director, el género y el año.
'''


import ast
import csv

filename = 'save.csv'

peliculas = []
print("Cargando base de datos de películas...")
with open(filename, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for fila in reader:
        if len(fila) == 17:
            peliculas.append(fila)
print("Base de datos lista.\n")

while True:
    try:
        title = input("Introduce el título de la película (o 'salir' para terminar): ").strip().lower()

        if not title:
            print("Por favor, escribe un título válido.\n")
            continue

        if title in ['salir', 'exit', 'q']:
            print("\n👋🏾Hasta luego.")
            break

        found = False

        for pelicula in peliculas:
            if title in pelicula[1].strip().lower():
                try:
                    actores = ast.literal_eval(pelicula[15])
                    actor_principal = actores[0] if actores else "Desconocido"
                except Exception:
                    actor_principal = "Desconocido"

                try:
                    generos = ", ".join(ast.literal_eval(pelicula[2]))
                except Exception:
                    generos = pelicula[2]

                print(f"\n{' DETALLES DE LA PELÍCULA ':=^40}")
                print(f"🎬 Título: {pelicula[1]}")
                print(f"👤 Actor principal: {actor_principal}")
                print(f"🎭 Género: {generos}")
                print(f"📅 Año: {pelicula[7]}")
                print("=" * 40 + "\n")
                found = True
                break

        if not found:
            print("❌ Película no encontrada.\n")

    except Exception as e:
        print(f"\n❌ Error: {e}\n")
