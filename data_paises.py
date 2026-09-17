'''
Crear una nueva lista a partir de la lista de paises con los siguientes datos:
- Nombre del país
- Densidad de Habitantes por km^2
- PIB per cápita
'''

# Lista de países con (Nombre, Población, PIB en €, Superficie en km²)
paises_eur = [
    ("España", 48000000, 1472000000000, 505990),
    ("México", 128500000, 1343200000000, 1964375),
    ("Estados Unidos", 335000000, 25760000000000, 9833520),
    ("China", 1410000000, 16560000000000, 9596961),
    ("Japón", 124500000, 3864000000000, 377975),
    ("Brasil", 215000000, 1978000000000, 8515767),
    ("Alemania", 84400000, 4048000000000, 357022),
    ("India", 1430000000, 3496000000000, 3287263),
    ("Francia", 68000000, 2760000000000, 551695),
    ("Argentina", 46200000, 588800000000, 2780400)
]

paises_data = [(pais[0], 
                f"{pais[1]/pais[3]:,.3f} hab/km²", 
                f"{pais[2]/pais[1]:,.2f} €",
                f"{pais[3]/1000:,.3f} km²")
for pais in paises_eur]

print(f"{'Nombre':15} | {'Densidad':<15} | {'PIB per cápita':<15} | {'Superficie':<15}")
print("-" * 65)

for pais in paises_data:
    print(f"{pais[0]:<15} | {pais[1]:<15} | {pais[2]:<15} | {pais[3]:<15}")


paises_densos = [pais for pais in paises_data if float(pais[1].replace(" hab/km²", "")) > 100]

print(f"\nPaíses con más de 100 hab/km²:")
print("-" * 65)
print(f"{'Nombre':15} | {'Densidad':<15} | {'PIB per cápita':<15} | {'Superficie':<15}")
print("-" * 65)

for pais in paises_densos:
    print(f"{pais[0]:<15} | {pais[1]:<15} | {pais[2]:<15} | {pais[3]:<15}")

menos_densos = [pais for pais in paises_data if float(pais[1].replace(" hab/km²", "")) < 100]

print(f"\nPaíses con menos de 100 hab/km²:")
print("-" * 65)
print(f"{'Nombre':15} | {'Densidad':<15} | {'PIB per cápita':<15} | {'Superficie':<15}")
print("-" * 65)
for pais in menos_densos:
    print(f"{pais[0]:<15} | {pais[1]:<15} | {pais[2]:<15} | {pais[3]:<15}")